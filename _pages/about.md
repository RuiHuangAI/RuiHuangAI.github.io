---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

#  About Me

Hello! 👏 I’m a third-year undergraduate student in **[UESTC’s “Everest Project”](https://www.uestc.edu.cn/%22%E5%AD%A6%E6%A0%A1%E5%AE%98%E7%BD%91%E2%80%9C)** Computer Top-Talent Experimental Class (2023–2027), majoring in Computer Science. Now, I’m interested in **LLM SFT/RL and reasoning, image/video generation, and unified multimodal models**. Earlier, I explored AI for smart grids and remote-sensing image fusion. You can find my [resume](https://ruihuangai.github.io/files/cv/RuiHuang_CV%202025.10.pdf) or [中文简历](https://ruihuangai.github.io/files/cv/RuiHuang_CV%20(Chinese)2025.10.pdf) here.

⭐  I am eager to discuss potential collaborations and am **actively seeking research internship opportunities(industry/academia),including onsite roles**.I ‘m also seeking for **2027 fall PHD position**. Please feel free to contact me via **email**: [huang_rui@std.uestc.edu.cn],[paulafixamiworali@gmail.com] or **WeChat: huangrui_dby** if you are interested.I warmly welcome your message and look forward to connecting!

# 🔥 News


- *2024.10*: &nbsp;🏆 I am happy to be awarded the **National Scholarship** of 2025.


- *2025.09*: &nbsp;🎉 We pre-released [**UniVA**](https://univa-agent.github.io/), first to unify Video **Understanding/Segmentation/Editing/Generation** into traceable multi-step workflows via Plan–Act agents, multi-level memory, and modular tools, plus UniVA-Bench!


- *2025.07*: &nbsp;🎉 I'm honored to be invited to be a reviewer of **AAAI 2026**!


- *2025.06*: &nbsp;🏆 I'm so happy to be 1/30 of **SenseTime Scholarship 2025!** *This is the greatest praise I have received so far.* 

- *2025.06*: &nbsp;🎉 We pre-released [**Diffusion Dataset Condensation**](https://arxiv.org/abs/2507.05914) on arXiv, **accelerating the pre-training of diffusion models by 100x**!!!. The entire project used **hundreds of H100/A100**!!

- *2025.06*: &nbsp;🎉 One paper has been accepted by [**IEEE Transactions on Industrial Informatics**](https://ieeexplore.ieee.org/abstract/document/11036164), completed during my first research internship in AI for smart grid.


- *2025.03*: &nbsp;🎉 We released [**CoT Image**](https://arxiv.org/abs/2501.13926), The first to **introduce CoT-style strategies into image generation**, it has attracted widespread attention in the community and received over **790+ stars**!!


- *2024.12*: &nbsp;🎉 Our paper [**Wavelet-Assisted Multi-Frequency Attention Network for Pansharpening**](https://ojs.aaai.org/index.php/AAAI/article/view/32381) has been accepted by **AAAI 2025** and selected for **Oral Presentation**. See you in Philadelphia!!!!



- *2024.10*: &nbsp;🏆 I am happy to be awarded the **National Scholarship** of 2024 and the **Gratitude Scholarship for Modern Scientists**.



- *2024.09*: &nbsp;🎉 One paper has been accepted by [**IEEE Transactions on Sustainable Energy**](https://ieeexplore.ieee.org/abstract/document/10679087/), completed during my first research internship in AI for smart grid.

- *2024.08*: &nbsp;🎉 I am delighted to be going to **Cambridge as a visiting student**.

- *2023.12*: &nbsp;🌱 The starting point of my academic journey.






# 📝 Selected Publications ＆ Preprints


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Under Review</div><img src='images/D2C.png' alt="D2C" style="width: 100%; height: auto; object-fit: cover; max-height: 200px;"></div></div>
<div class='paper-box-text' markdown="1">

[🔥Diffusion Dataset Condensation: Training Your Diffusion Model Faster with Less Data](https://arxiv.org/abs/2507.05914)

**Rui Huang**<sup style="font-size: 1.1em; position: relative; top: -2px;">*</sup> , Shitong Shao<sup style="font-size: 1.1em; position: relative; top: -2px;">*</sup> , Zikai Zhou, Pukun Zhao, Hangyu Guo, Tian Ye, Lichen Bai, Shuo Yang, Zeke Xie<sup>†</sup>



[**[PDF]**](https://arxiv.org/abs/2507.05914) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong> **[Github]**    <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>

**TL;DR:** *Proposed D²C: Diffusion Dataset Condensation for diffusion models, **enabling 100× faster training** with 0.8%–4% data via sample selection and semantic enhancement; **trained on hundreds of A800/H100 GPUs.***

</div>
</div>








<div class='paper-box'><div class='paper-box-image'><div><div class="badge">AAAI 2025 Oral</div><img src='images/WFANet.png' alt="D2C" style="width: 100%; height: auto; object-fit: cover; max-height: 200px;"></div></div>
<div class='paper-box-text' markdown="1">

[🔥Wavelet-Assisted Multi-Frequency Attention Network for Pansharpening](https://arxiv.org/pdf/2502.04903)

Jie Huang<sup style="font-size: 1.1em; position: relative; top: -2px;">*</sup>, **Rui Huang**<sup style="font-size: 1.1em; position: relative; top: -2px;">*</sup>, Jinghao Xu, Siran Pen, Yule Duan, Liangjian Deng<sup>†</sup>



[**[PDF]**](https://arxiv.org/pdf/2502.04903) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>    [**[Github]**](https://github.com/Jie-1203/WFANet) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>

**TL;DR:** *Proposed WFANet for image fusion, **combining wavelet transformation with attention**, achieving SOTA on multiple datasets.*

</div>
</div>



<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Under Review</div><img src='images/CoTImage.png' alt="D2C" style="width: 100%; height: auto; object-fit: cover; max-height: 200px;"></div></div>
<div class='paper-box-text' markdown="1">

[🔥Can We Generate Images with CoT? Let's Verify and Reinforce Image Generation Step by Step](https://arxiv.org/pdf/2501.13926)

Ziyu Guo<sup style="font-size: 1.1em; position: relative; top: -2px;">*</sup>, Renrui Zhang<sup style="font-size: 1.1em; position: relative; top: -2px;">*</sup><sup>†</sup>, Chengzhuo Tong<sup style="font-size: 1.1em; position: relative; top: -2px;">*</sup>, Zhizheng Zhao<sup style="font-size: 1.1em; position: relative; top: -2px;">*</sup>, **Rui Huang**, Haoquan Zhang, Manyuan Zhang, Jiaming Liu, Shanghang Zhang, Peng Gao, Hongsheng Li, Pheng-Ann Heng


[**[PDF]**](https://arxiv.org/pdf/2501.13926) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>    [**[Github🌟790+]**](https://github.com/ZiyuGuo99/Image-Generation-CoT) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>

**TL;DR:** *Proposed **CoT-Imag**e with step-wise reasoning and novel reward models (PARM/PARM++), improving autoregressive image generation by 24% via test-time verification and preference alignment.*


</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Under Review</div><img src='images/UniVA.png' alt="D2C" style="width: 100%; height: auto; object-fit: cover; max-height: 200px;"></div></div>
<div class='paper-box-text' markdown="1">


[🔥UniVA: Universal Video Agents towards Next-Generation Video Intelligence](https://univa-agent.github.io/)

Zhengyang Liang<sup style="font-size: 1.1em; position: relative; top: -2px;">*</sup>, Daoan Zhang<sup style="font-size: 1.1em; position: relative; top: -2px;">*</sup>, Huichi Zhou, **Rui Huang**, Bobo Li, Shengqiong Wu, Yuechen Zhang, Xiaohan Wang, Jiebo Luo, Lizi Liao, Hao Fei


[**[PDF]**](https://univa-agent.github.io/asserts/pdf/UniVA_ICLR2025_v4.pdf) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>    [**[HomePage]**](https://univa-agent.github.io/) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>


**TL;DR:** *UniVA unifies **understanding/segmentation/editing/generation** into traceable multi-step video workflows via Plan–Act agents, multi-level memory, and modular tools, plus UniVA-Bench.*

</div>
</div>



<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Under Review</div><img src='images/COLNet.png' alt="D2C" style="width: 100%; height: auto; object-fit: cover; max-height: 200px;"></div></div>
<div class='paper-box-text' markdown="1">

**Complementary Online Learning Network for Probabilistic Load Forecasting Against Extreme Weather**

**Rui Huang**, Pengfei Zhao, Di Cao<sup>†</sup>, Weihao Hu, Qi Huang, Zhe Chen


**[PDF]** <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>    **[Github]** <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>

**TL;DR:** *Proposed the Complementary Online Learning Network (COLNet) with a **Weather-aware gating mechanism for high precision probabilistic** and point forecasting under extreme weather.*

</div>
</div>



- [A Novel Spatiotemporal Pyramidal Graph Modeling Approach for Short-Term Residential Load Forecasting](https://ieeexplore.ieee.org/abstract/document/11036164)

  Pengfei Zhao, Weihao Hu, Di Cao<sup>†</sup>, **Rui Huang**, Xingtao Bai, Qi Huang, Zhe Chen

  **IEEE Transactions on Industrial Informatics** <span style="color:rgb(42, 25, 23); font-weight: bold; text-decoration: underline;">(SCI Q1, IF: 10.2)</span>



- [Causal Mechanism-Enabled Zero-Label Learning for Power Generation Forecasting of Newly-Built PV Sites](https://ieeexplore.ieee.org/abstract/document/10679087)

  Pengfei Zhao, Weihao Hu, Di Cao<sup>†</sup>, **Rui Huang**, Xiawei Wu, Qi Huang, Zhe Chen

  **IEEE Transactions on Sustainable Energy** <span style="color:rgb(46, 24, 21); font-weight: bold; text-decoration: underline;">(SCI Q1, IF: 7.9)</span>



# 📖 Educations
- *2023.09 - 2027.06*,  ["Everest Project"](https://www.peopleapp.com/rmharticle/30022294217) Computer Top Talent Experimental Class, University of Electronic Science and Technology of China



# 🏆 Honors
- [2025] **SenseTime Scholarship（商汤奖学金）** *(award rate <0.1%; 30 undergrads China-wide)* 
- [2025] **National Scholarship（国家奖学金）** *(top recipient in the college)* 
- [2024] **National Scholarship（国家奖学金）** *(top recipient in the college)* 
- [2024] **Gratitude Scholarship for Modern Scientists （感恩中国近现代科学家助学金）** *(top 10 in school)* 
- [2024] **Excellence Scholarship — School of Computer Science, UESTC** 
- [2024] **First-Class Scholarship for Outstanding Students** 

# 🏅 Competition Awards
- [2025] **National Gold Award — National College Student Career Planning Competition（职规赛国金）🏅** *(award rate <0.1%; first from UESTC to receive this award)* 
- [2025] **Provincial First Prize — China International College Students’ Innovation Competition （国创赛省一）🏅** 
- [2025] **Provincial Special Prize — “Challenge Cup” National College Students’ Extracurricular Academic and Technological Works Competition（挑战杯省特）🏅** 
- [2024] **National Third Prize — Five-Minute Research Presentation (5MRP) Competition🥉** 
- [2023] **Provincial First Prize — Huawei ICT Competition🏅（华为ICT省一）** *(rank 2rd in province)* 




# 💬 Talks ＆ Reports
- [2025.07]  [2025商汤奖学金公布！30位"AI新星"亮相](https://mp.weixin.qq.com/s?__biz=MzIwNTcyNzYwMA==&mid=2247517938&idx=1&sn=66103a3998e7b3755f32af5f3be6f75b&chksm=96e07ee6277e2872fd2e00976286c33afd25a3e466b2235657aa9a7f7e425bd2049666d1f09c&mpshare=1&scene=24&srcid=0718Inq5SGowPE7uvemNIILr&sharer_shareinfo=a746172ad5ef5bcbf81c2cc917ead121&sharer_shareinfo_first=a746172ad5ef5bcbf81c2cc917ead121&clicktime=1752772305&enterid=1752772305&ascene=14&devicetype=iOS18.5&version=18003d2c&nettype=WIFI&abtest_cookie=AAACAA%3D%3D&lang=zh_CN&countrycode=CN&fontScale=100&exportkey=n_ChQIAhIQqPwcIHfowKVjYOeA6C%2BHzhLfAQIE97dBBAEAAAAAAAghJgamoiYAAAAOpnltbLcz9gKNyK89dVj0cvYatumNjj57SbppV1In%2BGmhL5mBcw8dLpPMvsDQrln9KoP6Yqd5ipvH5ma9O85VWBRBdWS2XBPnJCnzIwnNWUNU%2FLQV0bePCOLpm7iqaVTSW%2FHug927DWs5Dof7AvC9CgCPSjJFZyehad4ikLg%2FKPIpvuldlclO8bVQlRa12SHXW9EOQNSAntdRDdlB%2B3G5z96%2BhAQMKZaAAOQ4jAqOFoW1RXF7l5vBUl1vhT3mhh0odgsSB9uRPS0%3D&pass_ticket=CNrTSQMfCS8c%2BMHFmEC1jRecvwJVfSjQ5iTcZBlPLU1LtfYC0lPWwK4T5Eq7Xv2K&wx_header=3) *-Interview by SenseTime*
- [2025.07]  [黄锐：“打造令人认可的中国AI产品”](https://ruihuangai.github.io/files/cv/5845817.pdf) *-Interview by Education Herald*
- [2025.04]  [🥇祝贺！全国金奖+2！](https://mp.weixin.qq.com/s/eoLKKNKcTUJcSMPlTtW2sA) *-Report by UESTC’s official account*
- [2025.04]  [【理想·担当 国奖风采】黄锐](https://mp.weixin.qq.com/s/OVhtz43FR5bH8AVfJMk1zg) *-Report by UESTC Student Financial Aid*
- [2024.10]  [【直播回放】电子科大AI社活动进行中](https://space.bilibili.com/3494373601839146?spm_id_from=333.788.upinfo.head.click) *-Report by UESTC Student Financial Aid*
- [2024.08]  [实践印记｜【致广大，尽精微】直播带货助力乡村经济，教育扶贫点亮希望之灯](https://mp.weixin.qq.com/s/x_NFfYF_0fYwwFT2cZkhKg) *-Report by UESTC Social Practice*



# 🎓 Services
- Reviewer for **AAAI 2026**
- Co-Founder of the **UESTC AI Club**
- Deputy captain for the **“Embrace the Great, Pursue the Subtle” Social Practice Team（“致广大 尽精微”实践队）**
