import mne
import matplotlib.pyplot as plt

subj_n = 1

folder_pth = {'baseline_folder': 'C:/FEL/ING/diplomka/data/baseline_stare/kamdu/',
       'trust_game_folder': 'C:/FEL/ING/diplomka/data/TG/kamdu/'
}

file_tags = {'baseline': 'HYSCAN_GD_JS_2024-12-09_13-12-25_Segment_0', #segment_0 is a short record. Seems like whole record is in segment_1
             'trust_game': 'HYSCAN_GD_JS_2024-12-09_13-24-23_Segment_0',

}

raw_data = mne.io.read_raw_edf(folder_pth['trust_game_folder']+file_tags['trust_game'] + '.edf', preload = True)


raw_data.plot()
plt.show()

for ann in raw_data.annotations:
    descr = ann["description"]
    start = ann["onset"]
    end = ann["onset"] + ann["duration"]
    print(f"'{descr}' goes from {start} to {end}")


raw_data.save(folder_pth['trust_game_folder']+file_tags['trust_game'] + '_bad_annot.fif', overwrite = True)


