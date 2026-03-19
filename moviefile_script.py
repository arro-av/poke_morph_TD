path = r"C:\path\to\your\img\files"

counter = 1

moviefiles = ["moviefilein1","moviefilein2"]

triggered_positive = False
triggered_negative = False

delay = op('constant1')['lfo_delay']

def onValueChange(channel, sampleIndex, val, prev):
    global triggered_positive, triggered_negative
    
    # set positive trigger flag | trigger stop_n_swap() at positive LFO peak
    if val >= 0.995 and not triggered_positive:
        triggered_positive = True 
        stop_n_swap()

    # set negative trigger flag | trigger stop_n_swap() at negative LFO peak
    if val <= -0.995 and not triggered_negative:
        triggered_negative = True
        stop_n_swap()

    # reset trigger flags
    if val < 0 and triggered_positive:
        triggered_positive = False
    if val > 0 and triggered_negative:
        triggered_negative = False


def stop_n_swap():
    global counter
    
    op('lfo1').par.play = 0

    run("op('lfo1').par.play = 1", delayFrames=delay)
    
    moviefile_to_update = "moviefilein1" if counter % 2 == 0 else "moviefilein2"
    new_pokemon = rf"{path}\pokemon ({counter}).png"
    
    op(moviefile_to_update).par.file = new_pokemon
    
    counter = (counter % 152) + 1
