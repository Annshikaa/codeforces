<h2><a href="https://codeforces.com/contest/12/problem/E" target="_blank" rel="noopener noreferrer">12E — Start of the session</a></h2>

| | |
|---|---|
| **Difficulty** | 2100 |
| **Language** | PyPy 3-64 |
| **Verdict** | ✅ Accepted |
| **Problem Link** | [Codeforces 12E](https://codeforces.com/contest/12/problem/E) |

## Topics
`constructive algorithms`

---

## Problem Statement

<div class="header"><div class="title">E. Start of the season</div><div class="time-limit"><div class="property-title">time limit per test</div>2 seconds</div><div class="memory-limit"><div class="property-title">memory limit per test</div>256 megabytes</div><div class="input-file input-standard" style="font-weight: bold"><div class="property-title">input</div>stdin</div><div class="output-file output-standard" style="font-weight: bold"><div class="property-title">output</div>stdout</div></div><div><p>Before the start of the football season in Berland a strange magic ritual is held. The most experienced magicians have to find a magic matrix of the size <span class="tex-span"><i>n</i> × <i>n</i></span> (<span class="tex-span"><i>n</i></span> is even number). Gods will never allow to start the championship without it. Matrix should contain integers from <span class="tex-span">0</span> to <span class="tex-span"><i>n</i> - 1</span>, main diagonal should contain only zeroes and matrix should be symmetric. Moreover, all numbers in each row should be different. Magicians are very tired of the thinking process, so they ask you to write a program to find such matrix.</p></div><div class="input-specification"><div class="section-title">Input</div><p>The first line contains one integer <span class="tex-span"><i>n</i></span> (<span class="tex-span">2 ≤ <i>n</i> ≤ 1000</span>), <span class="tex-span"><i>n</i></span> is even.</p></div><div class="output-specification"><div class="section-title">Output</div><p>Output <span class="tex-span"><i>n</i></span> lines with <span class="tex-span"><i>n</i></span> numbers each — the required matrix. Separate numbers with spaces. If there are several solutions, output any.</p></div><div class="sample-tests"><div class="section-title">Examples</div><div class="sample-test"><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id005083476007612101" id="id008497513546868048" class="input-output-copier">Copy</div></div><pre id="id005083476007612101">2<br></pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id00900391779414754" id="id00022714133910549328" class="input-output-copier">Copy</div></div><pre id="id00900391779414754">0 1<br>1 0<br></pre></div><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id005414846432655052" id="id0030473497954026263" class="input-output-copier">Copy</div></div><pre id="id005414846432655052">4<br></pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id0033266980301854376" id="id009363948072186522" class="input-output-copier">Copy</div></div><pre id="id0033266980301854376">0 1 3 2<br>1 0 2 3<br>3 2 0 1<br>2 3 1 0<br></pre></div></div></div>