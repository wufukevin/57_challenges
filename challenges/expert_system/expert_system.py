from utils.convertors import YesNoEnum, to_yes_no_enum
from utils.questioner import Questioner


class ExpSysRule:
    def __init__(self, question):
        self.question = question

    def __iter__(self):
        return self

    def __next__(self):
        raise StopIteration

    def set_answer(self, yes_no_enum):
        self.answer = yes_no_enum


class ReplaceBatteryRule(ExpSysRule):
    def __init__(self):
        super().__init__('Replace the battery.')

    def __next__(self):
        if self.answer == YesNoEnum.Yes:
            return


class CheckSparkPlugConnectionRule(ExpSysRule):
    def __init__(self):
        super().__init__('Check spark plug connections.')


class ContactSupportRule(ExpSysRule):
    def __init__(self):
        super().__init__('Get it in for service.')


class EnsureChokeRule(ExpSysRule):
    def __init__(self):
        super().__init__('Check to ensure the choke is opening and closing.')


class CheckFuelRule(ExpSysRule):
    def __init__(self):
        super().__init__('Does your car have fuel injection?')

    def __next__(self):
        if self.answer == YesNoEnum.Yes:
            return EnsureChokeRule()
        else:
            return ContactSupportRule()


class CheckEngineRule(ExpSysRule):
    def __init__(self):
        super().__init__('Does the engine start and then die?')

    def __next__(self):
        if self.answer == YesNoEnum.Yes:
            return CheckFuelRule()
        else:
            return ContactSupportRule()


class CheckCrankUpRule(ExpSysRule):
    def __init__(self):
        super().__init__('Does the car crank up but fail to start?')

    def __next__(self):
        if self.answer == YesNoEnum.Yes:
            return CheckSparkPlugConnectionRule()
        else:
            return CheckEngineRule()


class CheckClickingNoiseRule(ExpSysRule):
    def __init__(self):
        super().__init__('Does the car make a clicking noise?')

    def __next__(self):
        if self.answer == YesNoEnum.Yes:
            return ReplaceBatteryRule()
        else:
            return CheckCrankUpRule()


class CheckCarSilentRule(ExpSysRule):
    def __init__(self):
        super().__init__('Is the car silent when you turn the key?')

    def __next__(self):
        if self.answer == YesNoEnum.Yes:
            return CheckBatteryRule()
        else:
            return CheckClickingNoiseRule()


class CleanAndTryAgainRule(ExpSysRule):
    def __init__(self):
        super().__init__('Clean terminals and try starting again.')


class ReplaceCableAndTryAgainRule(ExpSysRule):
    def __init__(self):
        super().__init__('Replace cables and try again.')


class CheckBatteryRule(ExpSysRule):
    def __init__(self):
        super().__init__('Are the battery terminals corroded?')

    def __next__(self):
        if self.answer == YesNoEnum.Yes:
            return CleanAndTryAgainRule()
        else:
            return ReplaceCableAndTryAgainRule()


class ExpertSystem:
    def set_root_rule(self, rule):
        self.root_rule = rule

    def check_rules(self):
        last_rule = self.root_rule
        while True:
            try:
                questioner = Questioner().add_question(last_rule.question, to_yes_no_enum, True)
                answer, = questioner.ask()
                last_rule.set_answer(answer)
                last_rule = next(last_rule)
            except StopIteration:
                break
        return last_rule.question


if __name__ == '__main__':
    expert_system = ExpertSystem()
    rule = CheckCarSilentRule()
    expert_system.set_root_rule(rule)
    answer = expert_system.check_rules()
    print(answer)
