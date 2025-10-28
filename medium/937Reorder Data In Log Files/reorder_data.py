class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        digit_logs = []
        letter_logs = []
        # go through every log, put digit logs into digit_logs, same with letters
        for log in logs:
            if log[-1].isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append(log)
        # sort letter_logs first by contents, then by identifiers
        letter_logs.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        result = letter_logs + digit_logs
        return result

        