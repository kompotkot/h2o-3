package hex.infogram;

import hex.ModelBuilder;
import hex.ModelCategory;
import water.Key;

public class INFOGRAM extends ModelBuilder<INFOGRAMModel, INFOGRAMModel.INFOGRAMParameters, INFOGRAMModel.INFOGRAMOutput> {
  
  public INFOGRAM(boolean startup_once) { super(new INFOGRAMModel.INFOGRAMParameters(), startup_once);}
  
  public INFOGRAM(INFOGRAMModel.INFOGRAMParameters parms) {
    super(parms);
    init(false);
  }
  
  public INFOGRAM(INFOGRAMModel.INFOGRAMParameters parms, Key<INFOGRAMModel> key) {
    super(parms, key);
    init(false);
  }
  
  @Override
  protected Driver trainModelImpl() {
    return new INFOGRAMDriver();
  }

  @Override
  public ModelCategory[] can_build() {
    return new ModelCategory[] { ModelCategory.Binomial, ModelCategory.Multinomial};
  }

  @Override
  public boolean isSupervised() {
    return true;
  }

  @Override
  public BuilderVisibility builderVisibility() {
    return BuilderVisibility.Experimental;
  }
  
  @Override public boolean havePojo() { return false; }
  @Override public boolean haveMojo() { return false; }
  
  @Override
  public void init(boolean expensive) {
    super.init(expensive);
    if (expensive)
      validateINFOGRAMParameters();
  }
  
  private void validateINFOGRAMParameters() {
    // make sure sensitive_attributes are true predictor columns
    // make sure conditional_info threshold is between 0 and 1
    // make sure varimp threshold is between 0 and 1
  }
  
  private class INFOGRAMDriver extends Driver {

    @Override
    public void computeImpl() {
      
    }
  }
}
