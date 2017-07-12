# https://www.python.org/dev/peps/pep-0318/

import time


def debug_time(function_to_call):
    def inner_function(*args, **kwargs):
        print('---DEBUG START TIME FOR "{0}"'.format(function_to_call.__name__))
        # start_time = time.clock()
        # Deprecated since version 3.3: The behaviour of this function depends on the platform:
        # use perf_counter() or process_time() instead, depending on your requirements,
        # to have a well defined behaviour.
        # See also:
        # https://stackoverflow.com/questions/25785243/understanding-time-perf-counter-and-time-process-time/25787875#25787875
        """
There are two distincts types of 'time', in this context: absolute time and relative time.

Absolute time is the 'real-world time', which is returned by time.time() and which we are all used to deal with. 
It is usually measured from a fixed point in time in the past (e.g. the UNIX epoch of 00:00:00 UTC on 01/01/1970) 
at a resolution of at least 1 second. Modern systems usually provide milli- or micro-second resolution. 
It is maintained by the dedicated hardware on most computers, the RTC (real-time clock) circuit is normally 
battery powered so the system keeps track of real time between power ups. 
This 'real-world time' is also subject to modifications based on your location (time-zones) and season 
(daylight savings) or expressed as an offset from UTC (also known as GMT or Zulu time).

Secondly, there is relative time, which is returned by time.perf_counter and time.process_time. 
This type of time has no defined relationship to real-world time, in the sense that the relationship is 
system and implementation specific. It can be used only to measure time intervals, i.e. a unit-less value 
which is proportional to the time elapsed between two instants. 
This is mainly used to evaluate relative performance (e.g. whether this version of code runs faster than that 
version of code).

On modern systems, it is measured using a CPU counter which is monotonically increased at a frequency related 
to CPU's hardware clock. The counter resolution is highly dependent on the system's hardware, 
the value cannot be reliably related to real-world time or even compared between systems in most cases. 
Furthermore, the counter value is reset every time the CPU is powered up or reset.

time.perf_counter returns the absolute value of the counter. 
time.process_time is a value which is derived from the CPU counter but updated only when a given process is running 
on the CPU and can be broken down into 'user time', which is the time when the process itself is running on the CPU, 
and 'system time', which is the time when the operating system kernel is running on the CPU on behalf on the process.
"""
        start_time = time.perf_counter()
        value = function_to_call(*args, **kwargs)
        # end_time = time.clock()
        end_time = time.perf_counter()
        print('---DEBUG END TIME')
        print("---DEBUG TOOK {0:.4f} SEC.".format(end_time - start_time))
        return value

    return inner_function


@debug_time
def debugtest(sleep_how_long):
    time.sleep(sleep_how_long)


@debug_time
def debugtest2(what_to_print):
    time.sleep(1.5)
    print(what_to_print)


debugtest(2)
debugtest2('NEW TEST')
