#!/usr/bin/python3
import cmd


class ConsoleShow(cmd.Cmd):
    prompt = "Console >> "

    # def do_debug(self, args):
    #     print("Debug command executed")

    # def do_quit(self, args):
    #     print("Quitting...")
    #     return True

    def do_EOF(self, line):
        return True


if __name__ == "__main__":
    command = ConsoleShow()
    command.cmdloop()
