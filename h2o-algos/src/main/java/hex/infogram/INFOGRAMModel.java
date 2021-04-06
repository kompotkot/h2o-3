package hex.infogram;

import hex.Model;
import hex.ModelMetrics;
import water.Job;
import water.Key;

public class INFOGRAMModel extends Model<INFOGRAMModel, INFOGRAMModel.INFOGRAMParameters, INFOGRAMModel.INFOGRAMOutput> {
  /**
   * Full constructor
   *
   * @param selfKey
   * @param parms
   * @param output
   */
  public INFOGRAMModel(Key<INFOGRAMModel> selfKey, INFOGRAMParameters parms, INFOGRAMOutput output) {
    super(selfKey, parms, output);
  }

  @Override
  public ModelMetrics.MetricBuilder makeMetricBuilder(String[] domain) {
    return null;
  }

  @Override
  protected double[] score0(double[] data, double[] preds) {
    return new double[0];
  }

  public static class INFOGRAMParameters extends Model.Parameters {
    public Algorithm _algorithm = Algorithm.AUTO;  // default to AUTO algorithm
    public String _algorithm_params = new String();  // store user specific parameters for chosen algorithm
    public String[] _sensitive_attributes = null; // store sensitive features to be excluded from final model
    public double _conditional_info_threshold = 0.1;  // default set by Deep
    public double _varimp_threshold = 0.1;        // default set by Deep
    
    public enum Algorithm {
      AUTO,
      deeplearning,
      drf,
      gbm,
      glm,
      naivebayes,
      xgboost,
    }
    @Override
    public String algoName() {
      return "INFOGRAM";
    }

    @Override
    public String fullName() {
      return "INFOGRAM BUILDER";
    }

    @Override
    public String javaName() {
      return INFOGRAMModel.class.getName();
    }

    @Override
    public long progressUnits() {
      return 0;
    }
  }
  
  public static class INFOGRAMOutput extends Model.Output {
    public double[] _conditional_info;  // conditional info for admissible features in _admissible_features
    public double[] _varimp;  // varimp values for admissible features in _admissible_features
    public String[] _admissible_features; // predictors chosen that exceeds both conditional_info and varimp thresholds
    public INFOGRAMOutput() { super(); }
    
    public INFOGRAMOutput(Job job) { _job = job; }
    
    
  }
}
