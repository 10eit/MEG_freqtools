import utils.power_estimate

def search_key(pattern, string):
    if not isinstance(pattern, str) or not isinstance(string, str):
        raise TypeError("Both pattern and string must be strings")
        
    if pattern.lower() in string.lower():
        return string
    else:
        raise ValueError(f"Pattern '{pattern}' not found in string")

def freq_power_decoding(epochs, y_labels, clf, power_params, iir_filter, methods, decim):
    """
    epochs : MNE.Epochs Objects
    y_labels : numpy array or None
    clf : Sklearn Pipeline
    power_params : dict, with 'freq' label and 'cycle' label
    iir_filter : Bool, allow using iir_filter or not
    method : dict, method for calculating spectrum power and other params
    decim : int, downsampling rate.
    
    """
    if isinstance(power_params,dict):
        freq_list = power_params[search_key('freq',power_params.keys())]
        cycle_list = power_params[search_key('cycle',power_params.keys())]
        unsafe_estimate = utils.power_estimate.safe_power(epochs, freq_list, cycle_list)
        if unsafe_estimate and iir_filter:
            raise RuntimeWarning(
                """
                Consider to use Longer Signal or use IIR filter (However Unstable).\n
                Power Estimate will be distorted if your keep current settings.
                """
            )
    elif power_params == None:
        ## Use Safe Frequency Estimation Params
        print("Using Automatic Power Estimate Params")
        freq_list, cycle_list = utils.autocycle(epochs)
        print(f"Frequency Estimate from {freq_list[0]} to {freq_list[-1]}")

    if y_labels == None:
        y_labels = epochs.event_id # if label is not specified, use event label instead.

    epoch_data = epochs[cond]
    tfr = tfr_multitaper(
        epoch_data,
        freqs=freq_list,
        n_cycles=cycle_list,
        time_bandwidth=4,
        use_fft=True,
        return_itc=False,
        average=False,
        decim=decim,
        n_jobs=n_jobs
    )

    tfr.apply_baseline(baseline=(-0.1, 0), mode='logratio').crop(-0.1,1.6)
    
