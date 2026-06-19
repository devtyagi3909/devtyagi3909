# Dev Tyagi

**RTL & FPGA Design Engineer — AI Inference Silicon, Out-of-Order Microarchitecture, AXI Subsystems**

The AI industry's center of gravity has shifted from training to inference. Custom ASICs now command 40% of the inference accelerator market, the bottleneck has narrowed to a single discipline: writing RTL that moves data faster than arithmetic can consume it. That is the problem I work on.

Final-year ECE student at VIT Chennai. Interning at **IIT Palakkad** on neural network inference acceleration for Zynq-7000, and doing contract RTL work at **Vicharak** on RISC-V processor porting and SPI memory subsystems. My output is synthesizable, timed, and validated — not block diagrams.

---

## Projects

**Out-of-Order Superscalar RISC-V Processor** — `SystemVerilog` `UltraScale+`
Full RV32I superscalar core with Tomasulo's algorithm, ROB, CDB, speculative execution, and precise exception handling across a 7-stage pipeline. 250 MHz timing closure post-synthesis. >95% functional coverage closure. Passed full RISC-V ISA compliance suite.
**→ 1st Place + Special Jury Award, SanDisk Hardware Hackathon (100+ teams)**

**High-Throughput AXI4 DMA Engine** — `SystemVerilog` `PYNQ-Z2`
Interrupt-driven descriptor DMA with configurable burst lengths, AXI4-MM and AXI-Stream endpoints, and outstanding transaction tracking. 1 GB/s sustained throughput on real AXI traffic.
**→ 2nd Place, FPGA Makeathon**

**AXI4-Lite Verification IP** — `SystemVerilog` `UVM`
Full UVM testbench with constrained-random sequences, self-checking scoreboard, and SVA AMBA compliance checks. 100% functional coverage on address, data, and response channels.

**ConstraintForge** — `Tcl` `Python` `GitHub Actions` — [github.com/devtyagi3909/constraintforge](https://github.com/devtyagi3909/constraintforge)
Open-source annotated XDC/SDC/LPF constraint library for 14+ interfaces across 13 boards. Every file CI-validated on PR.
**[View the Live ConstraintForge Documentation](https://devtyagi3909.github.io/constraintforge/)**

---

## Stack

`SystemVerilog` `UVM` `SVA` `AXI4` `Vivado` `Zynq-7000` `UltraScale+` `ARM Cortex-A9 PS/PL` `STA` `CDC` `C/C++` `Tcl`

---

> The inference era does not reward generalists. It rewards engineers who can close timing, hit area budgets, and design the datapaths that silicon companies are paying to acquire.

[devtyagi3909@gmail.com](mailto:devtyagi3909@gmail.com) · [linkedin.com/in/devtyagi3909](https://linkedin.com/in/devtyagi3909) · [github.com/devtyagi3909](https://github.com/devtyagi3909)
