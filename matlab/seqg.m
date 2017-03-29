function re = seqg(varargin)
re = [];
for i = 1:numel(varargin)
    if isa( varargin{i}, 'function_handle' )
        re = [re varargin{i}() ];
    else
        re = [re varargin{i} ];
    end
end

