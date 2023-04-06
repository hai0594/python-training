import curses

def main(stdscr):
    # Clear screen
    stdscr.clear()

    # Define menu options
    options = ["Option 1", "Option 2", "Option 3", "Option 4"]

    # Highlighted option index
    highlighted_option_index = 0

    # Loop until user selects an option
    while True:
        # Print menu options
        for i, option in enumerate(options):
            if i == highlighted_option_index:
                stdscr.addstr(i, 0, option, curses.A_REVERSE)
            else:
                stdscr.addstr(i, 0, option)

        # Wait for user input
        key = stdscr.getch()

        # Move selection up
        if key == curses.KEY_UP:
            highlighted_option_index = (highlighted_option_index - 1) % len(options)

        # Move selection down
        elif key == curses.KEY_DOWN:
            highlighted_option_index = (highlighted_option_index + 1) % len(options)

        # Select option
        elif key == curses.KEY_ENTER or key in [10, 13]:
            break

    # Clear screen
    stdscr.clear()

# Run main function
curses.wrapper(main)