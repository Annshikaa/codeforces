<h2><a href="https://codeforces.com/contest/23/problem/B" target="_blank" rel="noopener noreferrer">23B — Party</a></h2>

| | |
|---|---|
| **Difficulty** | 1600 |
| **Language** | PyPy 3-64 |
| **Verdict** | ✅ Accepted |
| **Problem Link** | [Codeforces 23B](https://codeforces.com/contest/23/problem/B) |

## Topics
`constructive algorithms` `graphs` `math`

---

## Problem Statement

<div class="header"><div class="title">B. Party</div><div class="time-limit"><div class="property-title">time limit per test</div>2 seconds</div><div class="memory-limit"><div class="property-title">memory limit per test</div>256 megabytes</div><div class="input-file input-standard" style="font-weight: bold"><div class="property-title">input</div>stdin</div><div class="output-file output-standard" style="font-weight: bold"><div class="property-title">output</div>stdout</div></div><div><p><span class="tex-span"><i>n</i></span> people came to a party. Then those, who had no friends among people at the party, left. Then those, who had exactly 1 friend among those who stayed, left as well. Then those, who had exactly <span class="tex-span">2, 3, ..., <i>n</i> - 1</span> friends among those who stayed by the moment of their leaving, did the same.</p><p>What is the maximum amount of people that could stay at the party in the end? </p></div><div class="input-specification"><div class="section-title">Input</div><p>The first input line contains one number <span class="tex-span"><i>t</i></span> — amount of tests (<span class="tex-span">1 ≤ <i>t</i> ≤ 10<sup class="upper-index">5</sup></span>). Each of the following <span class="tex-span"><i>t</i></span> lines contains one integer number <span class="tex-span"><i>n</i></span> (<span class="tex-span">1 ≤ <i>n</i> ≤ 10<sup class="upper-index">5</sup></span>).</p></div><div class="output-specification"><div class="section-title">Output</div><p>For each test output in a separate line one number — the maximum amount of people that could stay in the end.</p></div><div class="sample-tests"><div class="section-title">Examples</div><div class="sample-test"><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id003983504281195883" id="id002942637034019753" class="input-output-copier">Copy</div></div><pre id="id003983504281195883">1<br>3<br></pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id003434002914907438" id="id006927089932757188" class="input-output-copier">Copy</div></div><pre id="id003434002914907438">1<br></pre></div></div></div>