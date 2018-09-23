
errors ='''
1	G-code words consist of a letter and a value. Letter was not found.
2	Numeric value format is not valid or missing an expected value.
3	Grbl '$' system command was not recognized or supported.
4	Negative value received for an expected positive value.
5	Homing cycle is not enabled via settings.
6	Minimum step pulse time must be greater than 3usec
7	EEPROM read failed. Reset and restored to default values.
8	Grbl '$' command cannot be used unless Grbl is IDLE. Ensures smooth operation during a job.
9	G-code locked out during alarm or jog state
10	Soft limits cannot be enabled without homing also enabled.
11	Max characters per line exceeded. Line was not processed and executed.
12	(Compile Option) Grbl '$' setting value exceeds the maximum step rate supported.
13	Safety door detected as opened and door state initiated.
14	(Grbl-Mega Only) Build info or startup line exceeded EEPROM line length limit.
15	Jog target exceeds machine travel. Command ignored.
16	Jog command with no '=' or contains prohibited g-code.
17	Laser mode requires PWM output.
20	Unsupported or invalid g-code command found in block.
21	More than one g-code command from same modal group found in block.
22	Feed rate has not yet been set or is undefined.
23	G-code command in block requires an integer value.
24	Two G-code commands that both require the use of the XYZ axis words were detected in the block.
25	A G-code word was repeated in the block.
26	A G-code command implicitly or explicitly requires XYZ axis words in the block, but none were detected.
27	N line number value is not within the valid range of 1 - 9,999,999.
28	A G-code command was sent, but is missing some required P or L value words in the line.
29	Grbl supports six work coordinate systems G54-G59. G59.1, G59.2, and G59.3 are not supported.
30	The G53 G-code command requires either a G0 seek or G1 feed motion mode to be active. A different motion was active.
31	There are unused axis words in the block and G80 motion mode cancel is active.
32	A G2 or G3 arc was commanded but there are no XYZ axis words in the selected plane to trace the arc.
33	The motion command has an invalid target. G2, G3, and G38.2 generates this error, if the arc is impossible to generate or if the probe target is the current position.
34	A G2 or G3 arc, traced with the radius definition, had a mathematical error when computing the arc geometry. Try either breaking up the arc into semi-circles or quadrants, or redefine them with the arc offset definition.
35	A G2 or G3 arc, traced with the offset definition, is missing the IJK offset word in the selected plane to trace the arc.
36	There are unused, leftover G-code words that aren't used by any command in the block.
37	The G43.1 dynamic tool length offset command cannot apply an offset to an axis other than its configured axis. The Grbl default axis is the Z-axis.
'''
errors = errors.split('\n')
errors = [e.strip() for e in errors]
errors = [e for e in errors if len(e)>0]
errors = [e.split('\t') for e in errors]
errors = [(e[0], e[1]) for e in errors]

d = {}
for e in errors:
    d[e[0]] = e[1]

errors = d
