<h2><a href="https://codeforces.com/contest/20/problem/A" target="_blank" rel="noopener noreferrer">20A — BerOS file system</a></h2>

| | |
|---|---|
| **Difficulty** | 1700 |
| **Language** | PyPy 3-64 |
| **Verdict** | ✅ Accepted |
| **Problem Link** | [Codeforces 20A](https://codeforces.com/contest/20/problem/A) |

## Topics
`implementation`

---

## Problem Statement

<div class="header"><div class="title">A. BerOS file system</div><div class="time-limit"><div class="property-title">time limit per test</div>2 seconds</div><div class="memory-limit"><div class="property-title">memory limit per test</div>64 megabytes</div><div class="input-file input-standard" style="font-weight: bold"><div class="property-title">input</div>stdin</div><div class="output-file output-standard" style="font-weight: bold"><div class="property-title">output</div>stdout</div></div><div><p>The new operating system BerOS has a nice feature. It is possible to use any number of characters <span class="tex-font-style-tt">'/'</span> as a delimiter in path instead of one traditional <span class="tex-font-style-tt">'/'</span>. For example, strings <span class="tex-font-style-tt">//usr///local//nginx/sbin//</span> and <span class="tex-font-style-tt">/usr/local/nginx///sbin</span> are equivalent. The character <span class="tex-font-style-tt">'/'</span> (or some sequence of such characters) at the end of the path is required only in case of the path to the root directory, which can be represented as single character <span class="tex-font-style-tt">'/'</span>.</p><p>A path called normalized if it contains the smallest possible number of characters <span class="tex-font-style-tt">'/'</span>.</p><p>Your task is to transform a given path to the normalized form.</p></div><div class="input-specification"><div class="section-title">Input</div><p>The first line of the input contains only lowercase Latin letters and character <span class="tex-font-style-tt">'/'</span> — the path to some directory. All paths start with at least one character <span class="tex-font-style-tt">'/'</span>. The length of the given line is no more than 100 characters, it is not empty.</p></div><div class="output-specification"><div class="section-title">Output</div><p>The path in normalized form.</p></div><div class="sample-tests"><div class="section-title">Examples</div><div class="sample-test"><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id0030446664718064886" id="id006935246350042381" class="input-output-copier">Copy</div></div><pre id="id0030446664718064886">//usr///local//nginx/sbin<br></pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id009312078355981174" id="id009802206810313161" class="input-output-copier">Copy</div></div><pre id="id009312078355981174">/usr/local/nginx/sbin<br></pre></div></div></div>