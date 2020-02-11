import unittest

from problog.program import PrologFile

from StructureLearning import StructureLearner


class StructureLearnerTest(unittest.TestCase):
    def test_learning(self):
        structure_learner = StructureLearner(PrologFile('surfing.data'))
        time_total = structure_learner.learn()
        print('================= FINAL THEORY =================')
        for rule in structure_learner.get_learned_rules():
            print(rule)
        print('==================== SCORES ====================')
        print('            Accuracy:\t', structure_learner.accuracy())
        print('           Precision:\t', structure_learner.precision())
        print('              Recall:\t', structure_learner.recall())
        print('================== STATISTICS ==================')
        for name, value in structure_learner.get_statistics():
            print('%20s:\t%s' % (name, value))
        print('          Total time:\t%.4fs' % time_total)
        self.assertTrue(True)

    def test_learning_with_logfile(self):
        structure_learner = StructureLearner(PrologFile('surfing.data'), log_file="log.txt")
        time_total = structure_learner.learn(max_rule_length=1, significance=0.5, beam_size=20)
        print('================= FINAL THEORY =================')
        for rule in structure_learner.get_learned_rules():
            print(rule)
        print('==================== SCORES ====================')
        print('            Accuracy:\t', structure_learner.accuracy())
        print('           Precision:\t', structure_learner.precision())
        print('              Recall:\t', structure_learner.recall())
        print('================== STATISTICS ==================')
        for name, value in structure_learner.get_statistics():
            print('%20s:\t%s' % (name, value))
        print('          Total time:\t%.4fs' % time_total)
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
