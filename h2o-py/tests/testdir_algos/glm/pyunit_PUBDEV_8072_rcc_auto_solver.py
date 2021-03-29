import sys
sys.path.insert(1,"../../../")
import h2o
from tests import pyunit_utils
from h2o.estimators.glm import H2OGeneralizedLinearEstimator as glm

# per michalk suggestion, if remove_collinear_columns=true, set solver to IRLSM from AUTO.
def test_glm_AUTO_solver():
    trainF = h2o.import_file(pyunit_utils.locate("smalldata/iris/iris_train.csv"))
    y = "species"
    x = [0,1,2,3]

    glmwoRCC = glm(family='multinomial', alpha=0, Lambda=0)
    glmwoRCC.train(training_frame=trainF, x=x, y=y)
    assert not('IRLSM'==glmwoRCC.actual_params['solver']) # default to Coordinate_descent for multinomial
    glmRCC = glm(family='multinomial', alpha=0, Lambda=0, remove_collinear_columns=True)
    glmRCC.train(training_frame=trainF, x=x, y=y)
    assert 'IRLSM'==glmRCC.actual_params['solver'], "Expected solver {0}, actual {1} and they are not equal." \
                                                    "".format("IRLSM", glmRCC.actual_params['solver'])

if __name__ == "__main__":
    pyunit_utils.standalone_test(test_glm_AUTO_solver)
else:
    test_glm_AUTO_solver()
