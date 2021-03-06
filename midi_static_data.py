MIDI_FOOTER = '''2, {last_tick}, End_track
3, 0, Start_track
3, 0, Title_t, {title}
3, 0, End_track
0, 0, End_of_file'''

MIDI_HEADER = '''0, 0, Header, 1, 3, 480
1, 0, Start_track
1, 0, Title_t, {title}
1, 0, Copyright_t, "Copyright � 2017 by Michael Seaman"
1, 0, SMPTE_offset, 96, 0, 3, 0, 0
1, 0, Time_signature, 4, 2, 24, 8
1, 0, Key_signature, 0, "major"
1, 0, Tempo, 500000
1, {last_tick}, End_track
2, 0, Start_track
2, 0, Title_t, "Piano"
2, 0, Program_c, 0, 1
2, 0, Control_c, 0, 7, 100
2, 0, Control_c, 0, 10, 64
2, 0, Control_c, 0, 91, 127
'''
