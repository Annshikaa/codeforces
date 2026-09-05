<h2><a href="https://codeforces.com/contest/23/problem/A" target="_blank" rel="noopener noreferrer">23A — You're Given a String...</a></h2>

| | |
|---|---|
| **Difficulty** | 1200 |
| **Language** | PyPy 3-64 |
| **Verdict** | ✅ Accepted |
| **Problem Link** | [Codeforces 23A](https://codeforces.com/contest/23/problem/A) |

## Topics
`brute force` `greedy`

---

## Problem Statement

<div class="header"><div class="title">A. You're Given a String...</div><div class="time-limit"><div class="property-title">time limit per test</div>2 seconds</div><div class="memory-limit"><div class="property-title">memory limit per test</div>256 megabytes</div><div class="input-file input-standard" style="font-weight: bold"><div class="property-title">input</div>stdin</div><div class="output-file output-standard" style="font-weight: bold"><div class="property-title">output</div>stdout</div></div><div><p>You're given a string of lower-case Latin letters. Your task is to find the length of its longest substring that can be met in the string at least twice. These occurrences can overlap (see sample test 2).</p></div><div class="input-specification"><div class="section-title">Input</div><p>The first input line contains the string. It's guaranteed, that the string is non-empty, consists of lower-case Latin letters, and its length doesn't exceed 100.</p></div><div class="output-specification"><div class="section-title">Output</div><p>Output one number — length of the longest substring that can be met in the string at least twice.</p></div><div class="sample-tests"><div class="section-title">Examples</div><div class="sample-test"><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id0007887838288976401" id="id007284613266444535" class="input-output-copier">Copy</div></div><pre id="id0007887838288976401">abcd<br></pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id003504966306946663" id="id0013539169165617893" class="input-output-copier">Copy</div></div><pre id="id003504966306946663">0</pre></div><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id0042929602605051853" id="id00594305713096257" class="input-output-copier">Copy</div></div><pre id="id0042929602605051853">ababa<br></pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id0015025352094494482" id="id001449452525991728" class="input-output-copier">Copy</div></div><pre id="id0015025352094494482">3</pre></div><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id003883570054728439" id="id0008889323457619891" class="input-output-copier">Copy</div></div><pre id="id003883570054728439">zzz<br></pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id004064275841813644" id="id008190634656447214" class="input-output-copier">Copy</div></div><pre id="id004064275841813644">2</pre></div></div></div>