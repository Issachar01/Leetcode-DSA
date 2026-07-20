class Solution:
    def interpret(self, command: str) -> str:
        goalParser = ""
        for i in range(len(command)):
            if command[i] == "G":
                goalParser = goalParser + "G"
            if command[i] == "(":
                if command[i+1] == ")":
                    goalParser = goalParser + "o"
                else:
                    goalParser = goalParser + "al"
        return goalParser