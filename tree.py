#!/usr/bin/env /Users/Shmuli/Library/Python/3.9/bin
import os
import sys

# Dictionary for file type icons
file_images = {
    # Programming Languages
    "py": "🐍 Python",
    "pyc": "🐍 Python Bytecode",
    "jsx": "🔮 JSX",
    "js": "🧩 JavaScript",
    "ts": "📜 TypeScript",
    "java": "☕ Java",
    "cpp": "💻 C++",
    "c": "🔧 C",
    "h": "🔧 C Header",
    "rb": "💎 Ruby",
    "go": "🐹 Go",
    "php": "🐘 PHP",
    "pl": "🖋️ Perl",
    "r": "📊 R",
    "swift": "🍎 Swift",
    "rs": "🦀 Rust",
    "dart": "🎯 Dart",
    "vue": "🔗 Vue",
    "scala": "🔮 Scala",
    "kotlin": "🧩 Kotlin",

    # Markup and Style
    "html": "🌐 HTML",
    "css": "🎨 CSS",
    "xml": "📜 XML",
    "yaml": "📜 YAML",
    "json": "🔢 JSON",
    "md": "📝 Markdown",

    # Scripts
    "sh": "🐚 Shell Script",
    "bat": "🖥️ Batch Script",
    "ps1": "⚙️ PowerShell Script",
    
    # Data
    "sql": "🔍 SQL",
    "csv": "📊 CSV",
    "tsv": "📊 TSV",
    "sqlite": "🔒 SQLite",
    
    # Configuration
    "ini": "⚙️ INI",
    "conf": "⚙️ Configuration",
    "properties": "⚙️ Properties",
    
    # Documentation and Others
    "pdf": "📄 PDF",
    "doc": "📄 DOC",
    "docx": "📄 DOCX",
    "xls": "📊 XLS",
    "xlsx": "📊 XLSX",
    "ppt": "📊 PPT",
    "pptx": "📊 PPTX",
    "log": "📝 Log",
    "txt": "📄 Text",
    "bz2": "📦 BZ2",
    "gz": "📦 GZ",
    "tar": "📦 TAR",
    "zip": "📦 ZIP",
    "rar": "📦 RAR",

    # Binary and Executable
    "exe": "💻 Executable",
    "dll": "🔧 DLL",
    "so": "🔧 SO",
    "app": "📦 App",
    "dmg": "📦 DMG"
}

# Colors for terminal output
blue = "\033[94m"
green = "\033[92m"
end = "\033[0m"

# Indentation and spacing
tab = "    "
extra_space = "  "

def get_file_icon(file_name):
    """Return the appropriate icon for the given file based on its extension."""
    _, ext = os.path.splitext(file_name)
    ext = ext.lstrip(".").lower()
    return file_images.get(ext, "📄")  # Default icon if extension not found

def display_directory(directory, level=0):
    """Recursively display the directory tree with color coding."""
    # Display the current directory
    print(f"{blue}{tab * level}📂 {directory}{end}", end="\n\n")
    
    # List and sort files and directories
    items = sorted(os.listdir(directory))
    
    for item in items:
        item_path = os.path.join(directory, item)
        
        if os.path.isdir(item_path):
            # Recursively display subdirectories
            display_directory(item_path, level + 1)
        else:
            # Display files with icons
            file_icon = get_file_icon(item)
            print(f"{extra_space}{tab * level}{green}{file_icon} {directory}/{item}{end}", end="\n\n")

def main():
    """Main function to handle command-line arguments and start the directory display."""
    if len(sys.argv) > 1:
        directory = sys.argv[1]
    else:
        directory = os.getcwd()

    if not os.path.isdir(directory):
        print(f"{blue}Error: '{directory}' is not a valid directory.{end}")
        sys.exit(1)

    print()
    display_directory(directory)

if __name__ == "__main__":
    main()
