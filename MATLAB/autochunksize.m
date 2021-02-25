function [chunksize] = autochunksize(data)
%AUTOCHUNKSIZE Attempt to generate a reasonable chunksize for dataset
%compression in an HDF5 file
% Strategy: divide all data dimensions by increasing powers of two until you reach
% about 1 MB per chunk
%
% I wish I didn't have to write this function.
% Why isn't auto-chunking already built into MATLAB's h5write? I just don't know.
%
% Written by Scott Feister on Feb 17 2021. 
    mywhos = whos('data');
    bytes_per_elem = mywhos.bytes / numel(data); % average bytes per data element
    target_numel = 1e6 / bytes_per_elem; % target number of data elements per chunk, for 1 MB chunks
    
    for i=0:100
        test_chunksize = ceil(size(data)/2^i);
        if prod(test_chunksize) < 2*target_numel
            chunksize = test_chunksize;
            return
        end
    end
    error("Error. \nFailed to find a good chunksize for this dataset.")
end
