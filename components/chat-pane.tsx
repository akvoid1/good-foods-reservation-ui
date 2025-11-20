'use client';

import { useState, useRef, useEffect } from 'react';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Card } from '@/components/ui/card';
import { Send, Loader2 } from 'lucide-react';
import { postMessage, AgentResponse } from '@/lib/api';
import { getSessionId } from '@/lib/session';

interface Message {
  id: string;
  role: 'user' | 'assistant';
  content: string;
  structured?: AgentResponse['structured'];
  suggested_replies?: string[];
}

interface ChatPaneProps {
  onVenueSelect?: (venues: any[]) => void;
}

export function ChatPane({ onVenueSelect }: ChatPaneProps) {
  const [messages, setMessages] = useState<Message[]>([
    {
      id: '1',
      role: 'assistant',
      content: "Hi — I'm GoodFoods. Tell me what kind of table you want or try: 'Table for 2 tonight at 8pm'.",
      suggested_replies: ['Table for 2 tonight', 'Find a nice place for 4', 'Show me Indian restaurants'],
    },
  ]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
  const messagesEndRef = useRef<HTMLDivElement>(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSendMessage = async (text: string) => {
    if (!text.trim()) return;

    const userMessage: Message = {
      id: `user_${Date.now()}`,
      role: 'user',
      content: text,
    };

    setMessages(prev => [...prev, userMessage]);
    setInput('');
    setLoading(true);

    try {
      const response = await postMessage({
        session_id: getSessionId(),
        message: text,
      });

      const assistantMessage: Message = {
        id: `asst_${Date.now()}`,
        role: 'assistant',
        content: response.text,
        structured: response.structured,
        suggested_replies: response.suggested_replies,
      };

      setMessages(prev => [...prev, assistantMessage]);

      if (response.structured?.venues && onVenueSelect) {
        onVenueSelect(response.structured.venues);
      }
    } catch (error) {
      const errorMessage: Message = {
        id: `error_${Date.now()}`,
        role: 'assistant',
        content: 'Sorry, something went wrong. Please try again.',
      };
      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex flex-col h-full bg-card rounded-lg border border-border">
      {/* Messages */}
      <div className="flex-1 overflow-y-auto p-4 space-y-4">
        {messages.map(message => (
          <div key={message.id} className={`flex ${message.role === 'user' ? 'justify-end' : 'justify-start'}`}>
            <div
              className={`max-w-xs lg:max-w-md px-4 py-2 rounded-lg ${
                message.role === 'user'
                  ? 'bg-primary text-primary-foreground rounded-br-none'
                  : 'bg-muted text-muted-foreground rounded-bl-none'
              }`}
            >
              <p className="text-sm">{message.content}</p>
              {message.suggested_replies && message.role === 'assistant' && (
                <div className="flex flex-wrap gap-2 mt-2">
                  {message.suggested_replies.slice(0, 3).map((reply, i) => (
                    <Button
                      key={i}
                      variant="outline"
                      size="sm"
                      onClick={() => handleSendMessage(reply)}
                      className="text-xs"
                    >
                      {reply}
                    </Button>
                  ))}
                </div>
              )}
            </div>
          </div>
        ))}
        {loading && (
          <div className="flex justify-start">
            <div className="bg-muted p-3 rounded-lg rounded-bl-none">
              <Loader2 className="w-4 h-4 animate-spin text-muted-foreground" />
            </div>
          </div>
        )}
        <div ref={messagesEndRef} />
      </div>

      {/* Input */}
      <div className="border-t border-border p-4 bg-card">
        <div className="flex gap-2">
          <Input
            value={input}
            onChange={e => setInput(e.target.value)}
            onKeyDown={e => e.key === 'Enter' && handleSendMessage(input)}
            placeholder="Tell me what you're looking for..."
            className="flex-1"
            disabled={loading}
          />
          <Button
            onClick={() => handleSendMessage(input)}
            disabled={loading || !input.trim()}
            className="gap-2"
          >
            <Send className="w-4 h-4" />
          </Button>
        </div>
      </div>
    </div>
  );
}
