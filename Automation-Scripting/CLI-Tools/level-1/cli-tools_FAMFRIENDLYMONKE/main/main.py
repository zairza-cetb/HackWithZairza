import sys
from cli_tools.cli import CLITool

def main():
    cli_tool = CLITool()

    if len(sys.argv) < 2:
        print("Usage: python main.py <feature> [options]")
        return

    feature = sys.argv[1]
    args = sys.argv[2:]

    cli_tool.execute(feature, args)

if __name__ == "__main__":
    main()