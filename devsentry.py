from scanner import load_patterns, scan_folder
import datetime
import json
import os
from colorama import Fore, Style, init

# Initialize colorama for Windows color support
init(autoreset=True)

def save_report(results, report_folder='reports/'):
    if not os.path.exists(report_folder):
        os.makedirs(report_folder)

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    report_filename = os.path.join(report_folder, f"scan_report_{timestamp}.json")

    with open(report_filename, 'w') as report_file:
        json.dump(results, report_file, indent=4)

    print(f"\n{Fore.GREEN}✅ Report saved to: {report_filename}\n")

def scan_option():
    folder_to_scan = input(f"\n{Fore.CYAN}📂 Enter folder path to scan (or press Enter for 'test_files'): ") or "test_files"

    print(f"{Fore.YELLOW}📁 Scanning folder: {folder_to_scan} ...")
    patterns = load_patterns()
    results = scan_folder(folder_to_scan, patterns)

    if results:
        print(f"\n{Fore.RED}⚠️  {len(results)} issues found!\n")
        for match in results:
            print(f"{Fore.MAGENTA}📄 File: {match['file']}")
            print(f"{Fore.BLUE}   🔎 Pattern: {match['pattern']}")
            print(f"{Fore.LIGHTBLACK_EX}   📌 Line {match['line_number']}: {match['match']}\n")
        save_report(results)
    else:
        print(f"\n{Fore.GREEN}✅ No sensitive patterns found!")

def view_last_report():
    try:
        report_files = sorted(os.listdir('reports/'), reverse=True)
        if not report_files:
            print(f"{Fore.RED}⚠️  No reports found!")
            return
        last_report = os.path.join('reports', report_files[0])
        with open(last_report, 'r') as file:
            data = json.load(file)
            print(f"\n{Fore.CYAN}📄 Last Scan Report:\n")
            for match in data:
                print(f"{Fore.MAGENTA}📄 File: {match['file']}")
                print(f"{Fore.BLUE}   🔎 Pattern: {match['pattern']}")
                print(f"{Fore.LIGHTBLACK_EX}   📌 Line {match['line_number']}: {match['match']}\n")
    except Exception as e:
        print(f"{Fore.RED}❌ Error reading report: {e}")

def main_menu():
    while True:
        print(f"\n{Fore.CYAN}🔰 DevSentry: Code Scanner Tool")
        print(f"{Fore.YELLOW}[1] Scan a Folder")
        print(f"{Fore.YELLOW}[2] View Last Report")
        print(f"{Fore.YELLOW}[3] Exit")
        
        choice = input(f"\n👉 Enter your choice: ").strip()

        if choice == '1':
            scan_option()
        elif choice == '2':
            view_last_report()
        elif choice == '3':
            print(f"{Fore.GREEN}👋 Exiting DevSentry. Goodbye!")
            break
        else:
            print(f"{Fore.RED}❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
