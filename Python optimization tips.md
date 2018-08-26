# Optimization Zen ☯️

0. Does an existing implementation already do what you need? (credit Ariel Rokem, @arokem)
1. Start with a reference implementation: slow, but clear
2. Test reference implementation
3. At any point, stop if performances are "good enough" (credit Boris Gorelik, @boris_gorelik)
3. Benchmark the reference implementation for bottlenecks
4. Focus on the "low-hanging fruits" first
5. Test each iteration against the reference implementation
7. Step-back: a different algorithm may yield better performances
8. Do not sacrifice clarity for speed...
9. ... although, if you must, do it as last step.

## Extra rules for scientific computing 📜

10. Start first with numpy vectorization
11. Do not forget about numexpr
11. Use Numba
12. Switch to Cython for more control or if you need to distribute a smaller self-contained package
13. To use multi-CPUs, release the GIL and use thread-based parallelism (joblib)

# Numba vs Cython 🏁

Both are excellent solutions. Which one to choose?

## Speed 🚀

- **Cython**: excellent performances 🏃🏃🏃🏃
- **Numba**: excellent performances (sometimes a bit faster than cython!) 🏃🏃🏃

🏆 **Winner**: Numba, but almost a tie (application dependent)


## Ease of use 😃

- **Cython**: *fair*
    - need to manully declare types and adding imports (more work than with Numba) 😐
    - Cython does not accept UTF-8 identifiers (α, β, γ, 😢)
    - Need duplicated code for a pure-python reference 😢
- **Numba**: *easy*
    - just decorate with @numba.jit 😃
    - A pure-python reference can be the same function *undecorated* 😃
    - Default arguments needs to be passed 😢

🏆 **Winner**: Numba


## Control optimization 🔧

- **Cython**: good understanding of how is optimized:
    - **HTML annotations:** see "python-hits" in C code to guide optimization
    - **line_profiler:** see which line takes the most time
- **Numba**: optimization is mostly a black-box. Either it works, or it doesn't. If things go wrong (fail to compile or poor performances) it is more of a guess work to understand why.

🏆 **Winner**: Cython


## Distribution 🚚 

- **Cython**: you can create small pre-compiled packages with no run-time dependencies (wheels or conda packages)
- **Numba**: has a *run-time dependency on LLVM*. LLVM is by default in Anaconda for all platforms, but still is a "big" dependency.

🏆 **Winner**: Cython


## Multi-platform development 💻 🚴🏿 🎮

- **Cython**: easy on Linux and macOS, compiler included in Anaconda. 
  A pain on Windows: need to install *MS Visual Studio 2015* (multi-GB) 
  and let Cython find it. Alternatively, on Windows 10 you can try the "native" Linux subsystem:
  [Using WSL and MobaXterm to Create a Linux Dev Environment on Windows](https://nickjanetakis.com/blog/using-wsl-and-mobaxterm-to-create-a-linux-dev-environment-on-windows).
- **Numba**: easy, the LVMM dependency is easy to install on Linux, macOS and Windows

🏆 **Winner**: Numba





