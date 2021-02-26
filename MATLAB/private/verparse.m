function [versionint] = verparse(version)
%VERPARSE Attempts to turn a version number into a large integer, for comparisons.
%   Simplistic, to say the least! Assumes a three-number version format of "1.0.1", for
%   example. Very simplistic. Won't work in general.

nums = strsplit(char(version), '.');

versionint = int64(str2double(nums(1))*1e6 + str2double(nums(2))*1e3 + str2double(nums(3)));

end