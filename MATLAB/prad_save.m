function prad_save(obj, h5filename)
    % prad_save Save any HDF5 file of a supported pradformat (e.g.
    % SimpleRadiograph, SimpleFields, etc.) into a MATLAB object
    %
    % This version of 'prad_save' is a stub function.
    % It is overloaded by an identically-named method within each respective Class
    % See MathWorks documentation article "Overload Functions in Class
    % Generation": https://www.mathworks.com/help/matlab/matlab_oop/overloading-functions-for-your-class.html?searchHighlight=overload%20functions&s_tid=srchtitle
    
    error(['Error.' newline 'Input object is of class "' class(obj) '" instead of one of the supported classes ("SimpleRadiograph", "AdvancedRadiograph", "SimpleFields", "ParticlesList", ...)' newline 'Is it possible you forgot to initialize your object with something like "rad = SimpleRadiograph;" or "fld = SimpleFields;" at the top of your MATLAB code, per the examples?']);