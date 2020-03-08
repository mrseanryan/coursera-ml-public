# machine learning - coursera [public]

This is a git workspace for the machine learning (ML) course on coursera.

PUBLIC repo - this does NOT contain answers to the course assignments.

This repo is shared as a place to collect links and notes, just in case it is useful.

## links

| link                                                                                                                               |
| ---------------------------------------------------------------------------------------------------------------------------------- |
| [the course](https://www.coursera.org/learn/machine-learning)                                                                      |
| [course wiki](https://share.coursera.org/wiki/index.php?title=ML:Main)                                                             |
| [git repo](https://github.com/mrseanryan/coursera-ml-public)                                                                       |
| [a students summary](http://www.luckycallor.com/index.php/2015/12/22/summary-of-course-machine-learning-by-andrew-ng-on-coursera/) |

## setup

- download octave 4.0.3:

[octave](https://ftp.gnu.org/gnu/octave/windows/)

- also install gnuplot 503:

[gnuplot](https://sourceforge.net/projects/gnuplot/?source=typ_redirect)

- optional - tell octave the path to gnuplot

```
notepad %USERPROFILE%\.octaverc
```

add this line:

```
gnuplot_binary 'c:\Program Files (x86)\gnuplot'
```

note: in the end I commented that out with a '%'.

- run octave CLI

- in octave CLI:

```
CD {path to this repo}
CD experiments

gfx
```

Two figures should be drawn, with plots.
