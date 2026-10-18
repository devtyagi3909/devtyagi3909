<p align="center">
  <img src="./assets/hero-telemetry.svg" width="100%" alt="dev tyagi // hardware &amp; runtime telemetry" />
</p>

<p align="center">
  <img src="./assets/terminal-boot.svg" width="100%" alt="systems telemetry boot" />
</p>

<p align="center">
  <img src="./assets/slash-divider.svg" width="100%" alt="divider" />
</p>



<p align="center">
  <a href="https://github.com/devtyagi3909"><img src="https://img.shields.io/badge/github-devtyagi3909-0D1117?style=flat-square&amp;logo=github&amp;logoColor=E6EDF3&amp;labelColor=161B22&amp;color=FF2E4D" alt="github" /></a>
  <a href="mailto:devtyagi3909@gmail.com"><img src="https://img.shields.io/badge/email-devtyagi3909%40gmail.com-0D1117?style=flat-square&amp;logo=gmail&amp;logoColor=E6EDF3&amp;labelColor=161B22&amp;color=FF2E4D" alt="email" /></a>
  <a href="https://linkedin.com/in/dev-tyagi3909"><img src="https://img.shields.io/badge/linkedin-dev--tyagi3909-0D1117?style=flat-square&amp;logo=linkedin&amp;logoColor=E6EDF3&amp;labelColor=161B22&amp;color=FF2E4D" alt="linkedin" /></a>
</p>

---

### // proof strip

```text
• 1st place + special jury award  : sandisk hardware hackathon (2-wide ooo rv32i core)
• 7 upstream contributions        : vllm, sglang, transformers, riscv-dbg, veer-eh1, cva6
• 49,133 of 49,152 tokens saved   : fixed nvfp4 marlin scale underflow on sm80-sm90 (sglang #45031)
• 0 stale token reads             : fixed rocm piecewise graph capture in vllm qwen4exp (#61486)
• sub-1ms inference @ 5w envelope : fpga axi4-stream dma acceleration on zynq-7000 soc
```

---

### // what i do

- **gpu inference**: upstream fixes in vllm and sglang. rocm piecewise graph capture, nvfp4 marlin scale underflow on sm80-sm90, vision weight loading on qwen3.5-vl, and cold-start time from eager xgrammar imports.
- **silicon**: built a 2-wide out-of-order rv32i core from scratch. tomasulo scheduling, dual rat, reservation stations, cdb broadcast, 7-stage pipeline, uvm testbench. 1st place at the sandisk hardware hackathon.
- **fpga + edge**: zynq-7000 designs with axi4 dma streaming (rf signal classification, int4 weight decompression), plus bare-metal firmware on stm32 and nrf.


