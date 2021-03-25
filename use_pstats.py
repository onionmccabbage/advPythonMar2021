import pstats
p = pstats.Stats('profiling_output')
p.print_stats()