#!/usr/bin/env python3
"""
MVC Reorganization Script
Reorganizes the project into proper MVC structure
"""

import os
import shutil
from pathlib import Path

# Color codes for output
GREEN = '\033[92m'
BLUE = '\033[94m'
YELLOW = '\033[93m'
RED = '\033[91m'
RESET = '\033[0m'

def print_step(message):
    print(f"{BLUE}➜{RESET} {message}")

def print_success(message):
    print(f"{GREEN}✓{RESET} {message}")

def print_warning(message):
    print(f"{YELLOW}⚠{RESET} {message}")

def print_error(message):
    print(f"{RED}✗{RESET} {message}")

class MVCReorganizer:
    def __init__(self):
        self.root = Path(".")
        self.moved_files = []
        self.errors = []
        
    def create_directories(self):
        """Create all necessary directories for MVC structure"""
        print_step("Creating directory structure...")
        
        # Frontend directories
        frontend_dirs = [
            "frontend/src/app",
            "frontend/src/components/ui",
            "frontend/src/views",
            "frontend/src/services",
            "frontend/src/hooks",
            "frontend/src/utils",
            "frontend/src/styles",
            "frontend/public",
        ]
        
        # Backend directories
        backend_dirs = [
            "backend-api/models",
            "backend-api/views",
            "backend-api/controllers",
            "backend-api/services",
            "backend-api/agent",
            "backend-api/config",
            "backend-api/utils",
        ]
        
        all_dirs = frontend_dirs + backend_dirs
        
        for dir_path in all_dirs:
            full_path = self.root / dir_path
            full_path.mkdir(parents=True, exist_ok=True)
            print_success(f"Created {dir_path}")
    
    def move_frontend_files(self):
        """Move frontend files to new structure"""
        print_step("Reorganizing frontend files...")
        
        moves = [
            # App directory
            ("app", "frontend/src/app"),
            
            # Components
            ("components", "frontend/src/components"),
            
            # Hooks
            ("hooks", "frontend/src/hooks"),
            
            # Public assets
            ("public", "frontend/public"),
            
            # Styles
            ("styles/globals.css", "frontend/src/styles/globals.css"),
            
            # Config files
            ("package.json", "frontend/package.json"),
            ("package-lock.json", "frontend/package-lock.json"),
            ("next.config.mjs", "frontend/next.config.mjs"),
            ("tsconfig.json", "frontend/tsconfig.json"),
            ("tailwind.config.ts", "frontend/tailwind.config.ts"),
            ("components.json", "frontend/components.json"),
            ("postcss.config.mjs", "frontend/postcss.config.mjs"),
            (".env.local", "frontend/.env.local"),
            (".env.example", "frontend/.env.example"),
            ("next-env.d.ts", "frontend/next-env.d.ts"),
        ]
        
        for src, dest in moves:
            self._move_file_or_dir(src, dest)
    
    def reorganize_frontend_lib(self):
        """Reorganize lib folder into services and utils"""
        print_step("Reorganizing frontend lib folder...")
        
        lib_moves = [
            ("lib/api.ts", "frontend/src/services/api-client.ts"),
            ("lib/session.ts", "frontend/src/utils/session.ts"),
            ("lib/utils.ts", "frontend/src/utils/cn.ts"),
        ]
        
        for src, dest in lib_moves:
            self._move_file_or_dir(src, dest)
    
    def move_backend_files(self):
        """Move backend files to new MVC structure"""
        print_step("Reorganizing backend files...")
        
        # Move main files
        main_moves = [
            ("backend/run.py", "backend-api/run.py"),
            ("backend/seed_data.py", "backend-api/seed_data.py"),
            ("backend/requirements.txt", "backend-api/requirements.txt"),
            ("backend/.env", "backend-api/.env"),
            ("backend/.env.example", "backend-api/.env.example"),
            ("backend/.gitignore", "backend-api/.gitignore"),
            ("backend/goodfoods.db", "backend-api/goodfoods.db"),
        ]
        
        for src, dest in main_moves:
            self._move_file_or_dir(src, dest)
        
        # Move app files
        app_moves = [
            ("backend/app/main.py", "backend-api/main.py"),
            ("backend/app/database.py", "backend-api/models/database.py"),
            ("backend/app/models.py", "backend-api/models/schemas.py"),
            ("backend/app/config.py", "backend-api/config/settings.py"),
        ]
        
        for src, dest in app_moves:
            self._move_file_or_dir(src, dest)
        
        # Move routers to controllers
        if (self.root / "backend/app/routers").exists():
            self._move_file_or_dir("backend/app/routers", "backend-api/controllers")
        
        # Move services
        if (self.root / "backend/app/services").exists():
            self._move_file_or_dir("backend/app/services", "backend-api/services")
        
        # Move agent
        if (self.root / "backend/app/agent").exists():
            self._move_file_or_dir("backend/app/agent", "backend-api/agent")
    
    def move_docs_and_tests(self):
        """Keep docs and tests at root level"""
        print_step("Organizing documentation and tests...")
        # These stay at root, no need to move
        print_success("Docs and tests remain at root level")
    
    def create_init_files(self):
        """Create __init__.py files for Python packages"""
        print_step("Creating __init__.py files...")
        
        python_dirs = [
            "backend-api",
            "backend-api/models",
            "backend-api/views",
            "backend-api/controllers",
            "backend-api/services",
            "backend-api/agent",
            "backend-api/config",
            "backend-api/utils",
        ]
        
        for dir_path in python_dirs:
            init_file = self.root / dir_path / "__init__.py"
            if not init_file.exists():
                init_file.touch()
                print_success(f"Created {dir_path}/__init__.py")
    
    def create_readme_files(self):
        """Create README files for each major directory"""
        print_step("Creating README files...")
        
        readmes = {
            "frontend/README.md": "# Frontend\n\nNext.js frontend with MVC architecture.\n\nSee main README.md for setup instructions.",
            "backend-api/README.md": "# Backend API\n\nFastAPI backend with MVC architecture.\n\nSee main README.md for setup instructions.",
        }
        
        for path, content in readmes.items():
            readme_path = self.root / path
            if not readme_path.exists():
                readme_path.write_text(content)
                print_success(f"Created {path}")
    
    def _move_file_or_dir(self, src, dest):
        """Helper to move file or directory"""
        src_path = self.root / src
        dest_path = self.root / dest
        
        if not src_path.exists():
            print_warning(f"Source not found: {src}")
            return
        
        try:
            # Create parent directory if needed
            dest_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Move the file or directory
            if dest_path.exists():
                print_warning(f"Destination exists, skipping: {dest}")
                return
            
            shutil.move(str(src_path), str(dest_path))
            self.moved_files.append((src, dest))
            print_success(f"Moved {src} → {dest}")
            
        except Exception as e:
            error_msg = f"Error moving {src} to {dest}: {e}"
            self.errors.append(error_msg)
            print_error(error_msg)
    
    def generate_report(self):
        """Generate reorganization report"""
        print_step("Generating report...")
        
        report = []
        report.append("# MVC Reorganization Report\n")
        report.append(f"## Summary\n")
        report.append(f"- Files moved: {len(self.moved_files)}\n")
        report.append(f"- Errors: {len(self.errors)}\n\n")
        
        if self.moved_files:
            report.append("## Moved Files\n")
            for src, dest in self.moved_files:
                report.append(f"- `{src}` → `{dest}`\n")
            report.append("\n")
        
        if self.errors:
            report.append("## Errors\n")
            for error in self.errors:
                report.append(f"- {error}\n")
            report.append("\n")
        
        report.append("## Next Steps\n")
        report.append("1. Update imports in moved files\n")
        report.append("2. Test backend: `cd backend-api && python run.py`\n")
        report.append("3. Test frontend: `cd frontend && npm run dev`\n")
        report.append("4. Run tests: `python tests/test_integration.py`\n")
        
        report_path = self.root / "MVC_REORGANIZATION_REPORT.md"
        report_path.write_text("".join(report))
        print_success(f"Report saved to {report_path}")
    
    def run(self):
        """Run the complete reorganization"""
        print(f"\n{BLUE}{'='*60}{RESET}")
        print(f"{BLUE}MVC Reorganization Script{RESET}")
        print(f"{BLUE}{'='*60}{RESET}\n")
        
        try:
            self.create_directories()
            self.move_frontend_files()
            self.reorganize_frontend_lib()
            self.move_backend_files()
            self.move_docs_and_tests()
            self.create_init_files()
            self.create_readme_files()
            self.generate_report()
            
            print(f"\n{GREEN}{'='*60}{RESET}")
            print(f"{GREEN}✓ Reorganization Complete!{RESET}")
            print(f"{GREEN}{'='*60}{RESET}\n")
            
            print("Summary:")
            print(f"  Files moved: {len(self.moved_files)}")
            print(f"  Errors: {len(self.errors)}")
            print(f"\nSee MVC_REORGANIZATION_REPORT.md for details.\n")
            
        except Exception as e:
            print_error(f"Fatal error: {e}")
            raise

if __name__ == "__main__":
    reorganizer = MVCReorganizer()
    reorganizer.run()
