<h2><a href="https://codeforces.com/contest/21/problem/D" target="_blank" rel="noopener noreferrer">21D — Traveling Graph</a></h2>

| | |
|---|---|
| **Difficulty** | 2400 |
| **Language** | PyPy 3-64 |
| **Verdict** | ✅ Accepted |
| **Problem Link** | [Codeforces 21D](https://codeforces.com/contest/21/problem/D) |

## Topics
`bitmasks` `graph matchings` `graphs`

---

## Problem Statement

<div class="header"><div class="title">D. Traveling Graph</div><div class="time-limit"><div class="property-title">time limit per test</div>0.5 second</div><div class="memory-limit"><div class="property-title">memory limit per test</div>64 megabytes</div><div class="input-file input-standard" style="font-weight: bold"><div class="property-title">input</div>stdin</div><div class="output-file output-standard" style="font-weight: bold"><div class="property-title">output</div>stdout</div></div><div><p>You are given undirected weighted graph. Find the length of the shortest cycle which starts from the vertex 1 and passes throught all the edges at least once. Graph may contain multiply edges between a pair of vertices and loops (edges from the vertex to itself).</p></div><div class="input-specification"><div class="section-title">Input</div><p>The first line of the input contains two integers <span class="tex-span"><i>n</i></span> and <span class="tex-span"><i>m</i></span> (<span class="tex-span">1 ≤ <i>n</i> ≤ 15, 0 ≤ <i>m</i> ≤ 2000</span>), <span class="tex-span"><i>n</i></span> is the amount of vertices, and <span class="tex-span"><i>m</i></span> is the amount of edges. Following <span class="tex-span"><i>m</i></span> lines contain edges as a triples <span class="tex-span"><i>x</i>, <i>y</i>, <i>w</i></span> (<span class="tex-span">1 ≤ <i>x</i>, <i>y</i> ≤ <i>n</i>, 1 ≤ <i>w</i> ≤ 10000</span>), <span class="tex-span"><i>x</i>, <i>y</i></span> are edge endpoints, and <span class="tex-span"><i>w</i></span> is the edge length.</p></div><div class="output-specification"><div class="section-title">Output</div><p>Output minimal cycle length or <span class="tex-font-style-tt">-1</span> if it doesn't exists.</p></div><div class="sample-tests"><div class="section-title">Examples</div><div class="sample-test"><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id006536090098168444" id="id006511339920549771" class="input-output-copier">Copy</div></div><pre id="id006536090098168444">3 3<br>1 2 1<br>2 3 1<br>3 1 1<br></pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id0029729419585831407" id="id0032768875324623703" class="input-output-copier">Copy</div></div><pre id="id0029729419585831407">3<br></pre></div><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id005606893382746828" id="id007357951593370924" class="input-output-copier">Copy</div></div><pre id="id005606893382746828">3 2<br>1 2 3<br>2 3 4<br></pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id0011841482204665899" id="id009643584659650414" class="input-output-copier">Copy</div></div><pre id="id0011841482204665899">14<br></pre></div></div></div>