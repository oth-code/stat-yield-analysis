import numpy as np

def basic_stats(x):
    x = np.asarray(x, dtype=float)
    return {
        "mean": float(np.mean(x)),
        "std_pop": float(np.std(x, ddof=0)),   
        "std_samp": float(np.std(x, ddof=1)), 
        "min": float(np.min(x)),
        "max": float(np.max(x)),
        "count": int(len(x)),
    }

def cp(mean, std, lsl, usl):
    # Cp = (USL - LSL) / (6σ)
    return (usl - lsl) / (6 * std) if std > 0 else np.nan

def cpk(mean, std, lsl, usl):
    # Cpk = min( (USL-mean)/(3σ), (mean-LSL)/(3σ) )
    if std <= 0:
        return np.nan
    cpu = (usl - mean) / (3 * std)
    cpl = (mean - lsl) / (3 * std)
    return min(cpu, cpl)