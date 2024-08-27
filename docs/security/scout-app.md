<h2>:mag: Vulnerabilities of <code>5ec652e2b5ae:latest</code></h2>

<details open="true"><summary>:package: Image Reference</strong> <code>5ec652e2b5ae:latest</code></summary>
<table>
<tr><td>digest</td><td><code>sha256:5ec652e2b5aed1a8230a17f133f675c84d21b95ac713cd29400d9197db4fb667</code></td><tr><tr><td>vulnerabilities</td><td><img alt="critical: 0" src="https://img.shields.io/badge/critical-0-lightgrey"/> <img alt="high: 3" src="https://img.shields.io/badge/high-3-e25d68"/> <img alt="medium: 1" src="https://img.shields.io/badge/medium-1-fbb552"/> <img alt="low: 38" src="https://img.shields.io/badge/low-38-fce1a9"/> <!-- unspecified: 0 --></td></tr>
<tr><td>size</td><td>3.7 GB</td></tr>
<tr><td>packages</td><td>348</td></tr>
</table>
</details></table>
</details>

<table>
<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 1" src="https://img.shields.io/badge/H-1-e25d68"/> <img alt="medium: 1" src="https://img.shields.io/badge/M-1-fbb552"/> <img alt="low: 0" src="https://img.shields.io/badge/L-0-lightgrey"/> <!-- unspecified: 0 --><strong>python-jose</strong> <code>3.3.0</code> (pypi)</summary>

<small><code>pkg:pypi/python-jose@3.3.0</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2024-33663?s=github&n=python-jose&t=pypi&vr=%3C%3D3.3.0"><img alt="high 7.4: CVE--2024--33663" src="https://img.shields.io/badge/CVE--2024--33663-lightgrey?label=high%207.4&labelColor=e25d68"/></a> <i>Use of a Broken or Risky Cryptographic Algorithm</i>

<table>
<tr><td>Affected range</td><td><code><=3.3.0</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>CVSS Score</td><td><code>7.4</code></td></tr>
<tr><td>CVSS Vector</td><td><code>CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:N</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.04%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>10th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

python-jose through 3.3.0 has algorithm confusion with OpenSSH ECDSA keys and other key formats. This is similar to CVE-2022-29217.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2024-33664?s=github&n=python-jose&t=pypi&vr=%3C%3D3.3.0"><img alt="medium 5.3: CVE--2024--33664" src="https://img.shields.io/badge/CVE--2024--33664-lightgrey?label=medium%205.3&labelColor=fbb552"/></a> <i>Uncontrolled Resource Consumption</i>

<table>
<tr><td>Affected range</td><td><code><=3.3.0</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>CVSS Score</td><td><code>5.3</code></td></tr>
<tr><td>CVSS Vector</td><td><code>CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:L</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.04%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>10th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

python-jose through 3.3.0 allows attackers to cause a denial of service (resource consumption) during a decode via a crafted JSON Web Encryption (JWE) token with a high compression ratio, aka a "JWT bomb." This is similar to CVE-2024-21319.

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 1" src="https://img.shields.io/badge/H-1-e25d68"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 0" src="https://img.shields.io/badge/L-0-lightgrey"/> <!-- unspecified: 0 --><strong>pip</strong> <code>24.2</code> (pypi)</summary>

<small><code>pkg:pypi/pip@24.2</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2018-20225?s=gitlab&n=pip&t=pypi&vr=%3E%3D0"><img alt="high 7.8: CVE--2018--20225" src="https://img.shields.io/badge/CVE--2018--20225-lightgrey?label=high%207.8&labelColor=e25d68"/></a> <i>OWASP Top Ten 2017 Category A9 - Using Components with Known Vulnerabilities</i>

<table>
<tr><td>Affected range</td><td><code>>=0</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>CVSS Score</td><td><code>7.8</code></td></tr>
<tr><td>CVSS Vector</td><td><code>CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.11%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>45th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

An issue was discovered in pip (all versions) because it installs the version with the highest version number, even if the user had intended to obtain a private package from a private index. This only affects use of the `--extra-index-url` option, and exploitation requires that the package does not already exist in the public index (and thus the attacker can put the package there with an arbitrary version number).

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 1" src="https://img.shields.io/badge/H-1-e25d68"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 0" src="https://img.shields.io/badge/L-0-lightgrey"/> <!-- unspecified: 0 --><strong>setuptools</strong> <code>65.5.1</code> (pypi)</summary>

<small><code>pkg:pypi/setuptools@65.5.1</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2024-6345?s=github&n=setuptools&t=pypi&vr=%3C70.0.0"><img alt="high 8.8: CVE--2024--6345" src="https://img.shields.io/badge/CVE--2024--6345-lightgrey?label=high%208.8&labelColor=e25d68"/></a> <i>Improper Control of Generation of Code ('Code Injection')</i>

<table>
<tr><td>Affected range</td><td><code><70.0.0</code></td></tr>
<tr><td>Fixed version</td><td><code>70.0.0</code></td></tr>
<tr><td>CVSS Score</td><td><code>8.8</code></td></tr>
<tr><td>CVSS Vector</td><td><code>CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.04%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>10th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A vulnerability in the `package_index` module of pypa/setuptools versions up to 69.1.1 allows for remote code execution via its download functions. These functions, which are used to download packages from URLs provided by users or retrieved from package index servers, are susceptible to code injection. If these functions are exposed to user-controlled inputs, such as package URLs, they can execute arbitrary commands on the system. The issue is fixed in version 70.0.

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 7" src="https://img.shields.io/badge/L-7-fce1a9"/> <!-- unspecified: 0 --><strong>glibc</strong> <code>2.31-13+deb11u10</code> (deb)</summary>

<small><code>pkg:deb/debian/glibc@2.31-13%2Bdeb11u10?os_distro=bullseye&os_name=debian&os_version=11</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2019-9192?s=debian&n=glibc&ns=debian&t=deb&osn=debian&osv=11&vr=%3E%3D2.31-13%2Bdeb11u10"><img alt="low : CVE--2019--9192" src="https://img.shields.io/badge/CVE--2019--9192-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.31-13+deb11u10</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.11%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>44th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

In the GNU C Library (aka glibc or libc6) through 2.29, check_dst_limits_calc_pos_1 in posix/regexec.c has Uncontrolled Recursion, as demonstrated by '(|)(\\1\\1)*' in grep, a different issue than CVE-2018-20796. NOTE: the software maintainer disputes that this is a vulnerability because the behavior occurs only with a crafted pattern

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2019-1010025?s=debian&n=glibc&ns=debian&t=deb&osn=debian&osv=11&vr=%3E%3D2.31-13%2Bdeb11u10"><img alt="low : CVE--2019--1010025" src="https://img.shields.io/badge/CVE--2019--1010025-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.31-13+deb11u10</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.35%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>72nd percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

GNU Libc current is affected by: Mitigation bypass. The impact is: Attacker may guess the heap addresses of pthread_created thread. The component is: glibc. NOTE: the vendor's position is "ASLR bypass itself is not a vulnerability.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2019-1010024?s=debian&n=glibc&ns=debian&t=deb&osn=debian&osv=11&vr=%3E%3D2.31-13%2Bdeb11u10"><img alt="low : CVE--2019--1010024" src="https://img.shields.io/badge/CVE--2019--1010024-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.31-13+deb11u10</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>3.02%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>91st percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

GNU Libc current is affected by: Mitigation bypass. The impact is: Attacker may bypass ASLR using cache of thread stack and heap. The component is: glibc. NOTE: Upstream comments indicate "this is being treated as a non-security bug and no real threat.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2019-1010023?s=debian&n=glibc&ns=debian&t=deb&osn=debian&osv=11&vr=%3E%3D2.31-13%2Bdeb11u10"><img alt="low : CVE--2019--1010023" src="https://img.shields.io/badge/CVE--2019--1010023-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.31-13+deb11u10</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>1.20%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>86th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

GNU Libc current is affected by: Re-mapping current loaded library with malicious ELF file. The impact is: In worst case attacker may evaluate privileges. The component is: libld. The attack vector is: Attacker sends 2 ELF files to victim and asks to run ldd on it. ldd execute code. NOTE: Upstream comments indicate "this is being treated as a non-security bug and no real threat.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2019-1010022?s=debian&n=glibc&ns=debian&t=deb&osn=debian&osv=11&vr=%3E%3D2.31-13%2Bdeb11u10"><img alt="low : CVE--2019--1010022" src="https://img.shields.io/badge/CVE--2019--1010022-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.31-13+deb11u10</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.41%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>74th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

GNU Libc current is affected by: Mitigation bypass. The impact is: Attacker may bypass stack guard protection. The component is: nptl. The attack vector is: Exploit stack buffer overflow vulnerability and use this bypass vulnerability to bypass stack guard. NOTE: Upstream comments indicate "this is being treated as a non-security bug and no real threat.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2018-20796?s=debian&n=glibc&ns=debian&t=deb&osn=debian&osv=11&vr=%3E%3D2.31-13%2Bdeb11u10"><img alt="low : CVE--2018--20796" src="https://img.shields.io/badge/CVE--2018--20796-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.31-13+deb11u10</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.44%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>75th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

In the GNU C Library (aka glibc or libc6) through 2.29, check_dst_limits_calc_pos_1 in posix/regexec.c has Uncontrolled Recursion, as demonstrated by '(\227|)(\\1\\1|t1|\\\2537)+' in grep.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2010-4756?s=debian&n=glibc&ns=debian&t=deb&osn=debian&osv=11&vr=%3E%3D2.31-13%2Bdeb11u10"><img alt="low : CVE--2010--4756" src="https://img.shields.io/badge/CVE--2010--4756-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.31-13+deb11u10</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.82%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>82nd percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

The glob implementation in the GNU C Library (aka glibc or libc6) allows remote authenticated users to cause a denial of service (CPU and memory consumption) via crafted glob expressions that do not match any pathnames, as demonstrated by glob expressions in STAT commands to an FTP daemon, a different vulnerability than CVE-2010-2632.

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 5" src="https://img.shields.io/badge/L-5-fce1a9"/> <!-- unspecified: 0 --><strong>systemd</strong> <code>247.3-7+deb11u5</code> (deb)</summary>

<small><code>pkg:deb/debian/systemd@247.3-7%2Bdeb11u5?os_distro=bullseye&os_name=debian&os_version=11</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2023-31439?s=debian&n=systemd&ns=debian&t=deb&osn=debian&osv=11&vr=%3E%3D247.3-7%2Bdeb11u5"><img alt="low : CVE--2023--31439" src="https://img.shields.io/badge/CVE--2023--31439-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=247.3-7+deb11u5</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.10%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>41st percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

An issue was discovered in systemd 253. An attacker can modify the contents of past events in a sealed log file and then adjust the file such that checking the integrity shows no error, despite modifications. NOTE: the vendor reportedly sent "a reply denying that any of the finding was a security vulnerability."

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2023-31438?s=debian&n=systemd&ns=debian&t=deb&osn=debian&osv=11&vr=%3E%3D247.3-7%2Bdeb11u5"><img alt="low : CVE--2023--31438" src="https://img.shields.io/badge/CVE--2023--31438-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=247.3-7+deb11u5</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.10%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>41st percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

An issue was discovered in systemd 253. An attacker can truncate a sealed log file and then resume log sealing such that checking the integrity shows no error, despite modifications. NOTE: the vendor reportedly sent "a reply denying that any of the finding was a security vulnerability."

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2023-31437?s=debian&n=systemd&ns=debian&t=deb&osn=debian&osv=11&vr=%3E%3D247.3-7%2Bdeb11u5"><img alt="low : CVE--2023--31437" src="https://img.shields.io/badge/CVE--2023--31437-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=247.3-7+deb11u5</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.09%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>39th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

An issue was discovered in systemd 253. An attacker can modify a sealed log file such that, in some views, not all existing and sealed log messages are displayed. NOTE: the vendor reportedly sent "a reply denying that any of the finding was a security vulnerability."

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2020-13529?s=debian&n=systemd&ns=debian&t=deb&osn=debian&osv=11&vr=%3E%3D247.3-7%2Bdeb11u5"><img alt="low : CVE--2020--13529" src="https://img.shields.io/badge/CVE--2020--13529-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=247.3-7+deb11u5</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.14%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>50th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

An exploitable denial-of-service vulnerability exists in Systemd 245. A specially crafted DHCP FORCERENEW packet can cause a server running the DHCP client to be vulnerable to a DHCP ACK spoofing attack. An attacker can forge a pair of FORCERENEW and DCHP ACK packets to reconfigure the server.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2013-4392?s=debian&n=systemd&ns=debian&t=deb&osn=debian&osv=11&vr=%3E%3D247.3-7%2Bdeb11u5"><img alt="low : CVE--2013--4392" src="https://img.shields.io/badge/CVE--2013--4392-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=247.3-7+deb11u5</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.04%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>5th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

systemd, when updating file permissions, allows local users to change the permissions and SELinux security contexts for arbitrary files via a symlink attack on unspecified files.

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 5" src="https://img.shields.io/badge/L-5-fce1a9"/> <!-- unspecified: 0 --><strong>pcre3</strong> <code>2:8.39-13</code> (deb)</summary>

<small><code>pkg:deb/debian/pcre3@2:8.39-13?os_distro=bullseye&os_name=debian&os_version=11</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2019-20838?s=debian&n=pcre3&ns=debian&t=deb&osn=debian&osv=11&vr=%3E%3D2%3A8.39-13"><img alt="low : CVE--2019--20838" src="https://img.shields.io/badge/CVE--2019--20838-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2:8.39-13</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>1.03%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>84th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

libpcre in PCRE before 8.43 allows a subject buffer over-read in JIT when UTF is disabled, and \X or \R has more than one fixed quantifier, a related issue to CVE-2019-20454.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2017-7246?s=debian&n=pcre3&ns=debian&t=deb&osn=debian&osv=11&vr=%3E%3D2%3A8.39-13"><img alt="low : CVE--2017--7246" src="https://img.shields.io/badge/CVE--2017--7246-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2:8.39-13</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.65%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>80th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

Stack-based buffer overflow in the pcre32_copy_substring function in pcre_get.c in libpcre1 in PCRE 8.40 allows remote attackers to cause a denial of service (WRITE of size 268) or possibly have unspecified other impact via a crafted file.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2017-7245?s=debian&n=pcre3&ns=debian&t=deb&osn=debian&osv=11&vr=%3E%3D2%3A8.39-13"><img alt="low : CVE--2017--7245" src="https://img.shields.io/badge/CVE--2017--7245-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2:8.39-13</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.65%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>80th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

Stack-based buffer overflow in the pcre32_copy_substring function in pcre_get.c in libpcre1 in PCRE 8.40 allows remote attackers to cause a denial of service (WRITE of size 4) or possibly have unspecified other impact via a crafted file.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2017-16231?s=debian&n=pcre3&ns=debian&t=deb&osn=debian&osv=11&vr=%3E%3D2%3A8.39-13"><img alt="low : CVE--2017--16231" src="https://img.shields.io/badge/CVE--2017--16231-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2:8.39-13</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.08%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>36th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

In PCRE 8.41, after compiling, a pcretest load test PoC produces a crash overflow in the function match() in pcre_exec.c because of a self-recursive call. NOTE: third parties dispute the relevance of this report, noting that there are options that can be used to limit the amount of stack that is used

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2017-11164?s=debian&n=pcre3&ns=debian&t=deb&osn=debian&osv=11&vr=%3E%3D2%3A8.39-13"><img alt="low : CVE--2017--11164" src="https://img.shields.io/badge/CVE--2017--11164-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2:8.39-13</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.37%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>73rd percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

In PCRE 8.41, the OP_KETRMAX feature in the match function in pcre_exec.c allows stack exhaustion (uncontrolled recursion) when processing a crafted regular expression.

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 3" src="https://img.shields.io/badge/L-3-fce1a9"/> <!-- unspecified: 0 --><strong>shadow</strong> <code>1:4.8.1-1</code> (deb)</summary>

<small><code>pkg:deb/debian/shadow@1:4.8.1-1?os_distro=bullseye&os_name=debian&os_version=11</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2019-19882?s=debian&n=shadow&ns=debian&t=deb&osn=debian&osv=11&vr=%3E%3D1%3A4.8.1-1"><img alt="low : CVE--2019--19882" src="https://img.shields.io/badge/CVE--2019--19882-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=1:4.8.1-1</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.04%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>5th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

shadow 4.8, in certain circumstances affecting at least Gentoo, Arch Linux, and Void Linux, allows local users to obtain root access because setuid programs are misconfigured. Specifically, this affects shadow 4.8 when compiled using --with-libpam but without explicitly passing --disable-account-tools-setuid, and without a PAM configuration suitable for use with setuid account management tools. This combination leads to account management tools (groupadd, groupdel, groupmod, useradd, userdel, usermod) that can easily be used by unprivileged local users to escalate privileges to root in multiple ways. This issue became much more relevant in approximately December 2019 when an unrelated bug was fixed (i.e., the chmod calls to suidusbins were fixed in the upstream Makefile which is now included in the release version 4.8).

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2013-4235?s=debian&n=shadow&ns=debian&t=deb&osn=debian&osv=11&vr=%3E%3D1%3A4.8.1-1"><img alt="low : CVE--2013--4235" src="https://img.shields.io/badge/CVE--2013--4235-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=1:4.8.1-1</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.05%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>18th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

shadow: TOCTOU (time-of-check time-of-use) race condition when copying and removing directory trees

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2007-5686?s=debian&n=shadow&ns=debian&t=deb&osn=debian&osv=11&vr=%3E%3D1%3A4.8.1-1"><img alt="low : CVE--2007--5686" src="https://img.shields.io/badge/CVE--2007--5686-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=1:4.8.1-1</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.15%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>51st percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

initscripts in rPath Linux 1 sets insecure permissions for the /var/log/btmp file, which allows local users to obtain sensitive information regarding authentication attempts.  NOTE: because sshd detects the insecure permissions and does not log certain events, this also prevents sshd from logging failed authentication attempts by remote attackers.

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 3" src="https://img.shields.io/badge/L-3-fce1a9"/> <!-- unspecified: 0 --><strong>expat</strong> <code>2.2.10-2+deb11u5</code> (deb)</summary>

<small><code>pkg:deb/debian/expat@2.2.10-2%2Bdeb11u5?os_distro=bullseye&os_name=debian&os_version=11</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2024-28757?s=debian&n=expat&ns=debian&t=deb&osn=debian&osv=11&vr=%3E%3D2.2.10-2%2Bdeb11u5"><img alt="low : CVE--2024--28757" src="https://img.shields.io/badge/CVE--2024--28757-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.2.10-2+deb11u5</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.04%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>11th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

libexpat through 2.6.1 allows an XML Entity Expansion attack when there is isolated use of external parsers (created via XML_ExternalEntityParserCreate).

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2023-52426?s=debian&n=expat&ns=debian&t=deb&osn=debian&osv=11&vr=%3E%3D2.2.10-2%2Bdeb11u5"><img alt="low : CVE--2023--52426" src="https://img.shields.io/badge/CVE--2023--52426-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.2.10-2+deb11u5</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.05%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>21st percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

libexpat through 2.5.0 allows recursive XML Entity Expansion if XML_DTD is undefined at compile time.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2013-0340?s=debian&n=expat&ns=debian&t=deb&osn=debian&osv=11&vr=%3E%3D2.2.10-2%2Bdeb11u5"><img alt="low : CVE--2013--0340" src="https://img.shields.io/badge/CVE--2013--0340-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.2.10-2+deb11u5</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.52%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>77th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

expat 2.1.0 and earlier does not properly handle entities expansion unless an application developer uses the XML_SetEntityDeclHandler function, which allows remote attackers to cause a denial of service (resource consumption), send HTTP requests to intranet servers, or read arbitrary files via a crafted XML document, aka an XML External Entity (XXE) issue.  NOTE: it could be argued that because expat already provides the ability to disable external entity expansion, the responsibility for resolving this issue lies with application developers; according to this argument, this entry should be REJECTed, and each affected application would need its own CVE.

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 3" src="https://img.shields.io/badge/L-3-fce1a9"/> <!-- unspecified: 0 --><strong>sqlite3</strong> <code>3.34.1-3</code> (deb)</summary>

<small><code>pkg:deb/debian/sqlite3@3.34.1-3?os_distro=bullseye&os_name=debian&os_version=11</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2022-35737?s=debian&n=sqlite3&ns=debian&t=deb&osn=debian&osv=11&vr=%3E%3D3.34.1-3"><img alt="low : CVE--2022--35737" src="https://img.shields.io/badge/CVE--2022--35737-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=3.34.1-3</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.25%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>66th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

SQLite 1.0.12 through 3.39.x before 3.39.2 sometimes allows an array-bounds overflow if billions of bytes are used in a string argument to a C API.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2021-45346?s=debian&n=sqlite3&ns=debian&t=deb&osn=debian&osv=11&vr=%3E%3D3.34.1-3"><img alt="low : CVE--2021--45346" src="https://img.shields.io/badge/CVE--2021--45346-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=3.34.1-3</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.22%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>61st percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A Memory Leak vulnerability exists in SQLite Project SQLite3 3.35.1 and 3.37.0 via maliciously crafted SQL Queries (made via editing the Database File), it is possible to query a record, and leak subsequent bytes of memory that extend beyond the record, which could let a malicious user obtain sensitive information. NOTE: The developer disputes this as a vulnerability stating that If you give SQLite a corrupted database file and submit a query against the database, it might read parts of the database that you did not intend or expect.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2021-36690?s=debian&n=sqlite3&ns=debian&t=deb&osn=debian&osv=11&vr=%3E%3D3.34.1-3"><img alt="low : CVE--2021--36690" src="https://img.shields.io/badge/CVE--2021--36690-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=3.34.1-3</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.43%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>75th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A segmentation fault can occur in the sqlite3.exe command-line component of SQLite 3.36.0 via the idxGetTableInfo function when there is a crafted SQL query. NOTE: the vendor disputes the relevance of this report because a sqlite3.exe user already has full privileges (e.g., is intentionally allowed to execute commands). This report does NOT imply any problem in the SQLite library.

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 2" src="https://img.shields.io/badge/L-2-fce1a9"/> <!-- unspecified: 0 --><strong>perl</strong> <code>5.32.1-4+deb11u3</code> (deb)</summary>

<small><code>pkg:deb/debian/perl@5.32.1-4%2Bdeb11u3?os_distro=bullseye&os_name=debian&os_version=11</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2023-31486?s=debian&n=perl&ns=debian&t=deb&osn=debian&osv=11&vr=%3E%3D5.32.1-4%2Bdeb11u3"><img alt="low : CVE--2023--31486" src="https://img.shields.io/badge/CVE--2023--31486-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=5.32.1-4+deb11u3</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.33%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>71st percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

HTTP::Tiny before 0.083, a Perl core module since 5.13.9 and available standalone on CPAN, has an insecure default TLS configuration where users must opt in to verify certificates.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2011-4116?s=debian&n=perl&ns=debian&t=deb&osn=debian&osv=11&vr=%3E%3D5.32.1-4%2Bdeb11u3"><img alt="low : CVE--2011--4116" src="https://img.shields.io/badge/CVE--2011--4116-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=5.32.1-4+deb11u3</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.24%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>65th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

_is_safe in the File::Temp module for Perl does not properly handle symlinks.

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 1" src="https://img.shields.io/badge/L-1-fce1a9"/> <!-- unspecified: 0 --><strong>gnupg2</strong> <code>2.2.27-2+deb11u2</code> (deb)</summary>

<small><code>pkg:deb/debian/gnupg2@2.2.27-2%2Bdeb11u2?os_distro=bullseye&os_name=debian&os_version=11</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2022-3219?s=debian&n=gnupg2&ns=debian&t=deb&osn=debian&osv=11&vr=%3E%3D2.2.27-2%2Bdeb11u2"><img alt="low : CVE--2022--3219" src="https://img.shields.io/badge/CVE--2022--3219-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.2.27-2+deb11u2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.05%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>18th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

GnuPG can be made to spin on a relatively small input by (for example) crafting a public key with thousands of signatures attached, compressed down to just a few KB.

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 1" src="https://img.shields.io/badge/L-1-fce1a9"/> <!-- unspecified: 0 --><strong>openssl</strong> <code>1.1.1w-0+deb11u1</code> (deb)</summary>

<small><code>pkg:deb/debian/openssl@1.1.1w-0%2Bdeb11u1?os_distro=bullseye&os_name=debian&os_version=11</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2010-0928?s=debian&n=openssl&ns=debian&t=deb&osn=debian&osv=11&vr=%3E%3D1.1.1w-0%2Bdeb11u1"><img alt="low : CVE--2010--0928" src="https://img.shields.io/badge/CVE--2010--0928-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=1.1.1w-0+deb11u1</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.07%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>30th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

OpenSSL 0.9.8i on the Gaisler Research LEON3 SoC on the Xilinx Virtex-II Pro FPGA uses a Fixed Width Exponentiation (FWE) algorithm for certain signature calculations, and does not verify the signature before providing it to a caller, which makes it easier for physically proximate attackers to determine the private key via a modified supply voltage for the microprocessor, related to a "fault-based attack."

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 1" src="https://img.shields.io/badge/L-1-fce1a9"/> <!-- unspecified: 0 --><strong>libgcrypt20</strong> <code>1.8.7-6</code> (deb)</summary>

<small><code>pkg:deb/debian/libgcrypt20@1.8.7-6?os_distro=bullseye&os_name=debian&os_version=11</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2018-6829?s=debian&n=libgcrypt20&ns=debian&t=deb&osn=debian&osv=11&vr=%3E%3D1.8.7-6"><img alt="low : CVE--2018--6829" src="https://img.shields.io/badge/CVE--2018--6829-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=1.8.7-6</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.19%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>57th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

cipher/elgamal.c in Libgcrypt through 1.8.2, when used to encrypt messages directly, improperly encodes plaintexts, which allows attackers to obtain sensitive information by reading ciphertext data (i.e., it does not have semantic security in face of a ciphertext-only attack). The Decisional Diffie-Hellman (DDH) assumption does not hold for Libgcrypt's ElGamal implementation.

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 1" src="https://img.shields.io/badge/L-1-fce1a9"/> <!-- unspecified: 0 --><strong>gnutls28</strong> <code>3.7.1-5+deb11u5</code> (deb)</summary>

<small><code>pkg:deb/debian/gnutls28@3.7.1-5%2Bdeb11u5?os_distro=bullseye&os_name=debian&os_version=11</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2011-3389?s=debian&n=gnutls28&ns=debian&t=deb&osn=debian&osv=11&vr=%3E%3D3.7.1-5%2Bdeb11u5"><img alt="low : CVE--2011--3389" src="https://img.shields.io/badge/CVE--2011--3389-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=3.7.1-5+deb11u5</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.85%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>83rd percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

The SSL protocol, as used in certain configurations in Microsoft Windows and Microsoft Internet Explorer, Mozilla Firefox, Google Chrome, Opera, and other products, encrypts data by using CBC mode with chained initialization vectors, which allows man-in-the-middle attackers to obtain plaintext HTTP headers via a blockwise chosen-boundary attack (BCBA) on an HTTPS session, in conjunction with JavaScript code that uses (1) the HTML5 WebSocket API, (2) the Java URLConnection API, or (3) the Silverlight WebClient API, aka a "BEAST" attack.

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 1" src="https://img.shields.io/badge/L-1-fce1a9"/> <!-- unspecified: 0 --><strong>krb5</strong> <code>1.18.3-6+deb11u5</code> (deb)</summary>

<small><code>pkg:deb/debian/krb5@1.18.3-6%2Bdeb11u5?os_distro=bullseye&os_name=debian&os_version=11</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2018-5709?s=debian&n=krb5&ns=debian&t=deb&osn=debian&osv=11&vr=%3E%3D1.18.3-6%2Bdeb11u4"><img alt="low : CVE--2018--5709" src="https://img.shields.io/badge/CVE--2018--5709-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=1.18.3-6+deb11u4</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.10%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>41st percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

An issue was discovered in MIT Kerberos 5 (aka krb5) through 1.16. There is a variable "dbentry->n_key_data" in kadmin/dbutil/dump.c that can store 16-bit data but unknowingly the developer has assigned a "u4" variable to it, which is for 32-bit data. An attacker can use this vulnerability to affect other artifacts of the database as we know that a Kerberos database dump file contains trusted data.

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 1" src="https://img.shields.io/badge/L-1-fce1a9"/> <!-- unspecified: 0 --><strong>util-linux</strong> <code>2.36.1-8+deb11u2</code> (deb)</summary>

<small><code>pkg:deb/debian/util-linux@2.36.1-8%2Bdeb11u2?os_distro=bullseye&os_name=debian&os_version=11</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2022-0563?s=debian&n=util-linux&ns=debian&t=deb&osn=debian&osv=11&vr=%3E%3D2.36.1-8%2Bdeb11u2"><img alt="low : CVE--2022--0563" src="https://img.shields.io/badge/CVE--2022--0563-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.36.1-8+deb11u2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.05%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>18th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A flaw was found in the util-linux chfn and chsh utilities when compiled with Readline support. The Readline library uses an "INPUTRC" environment variable to get a path to the library config file. When the library cannot parse the specified file, it prints an error message containing data from the file. This flaw allows an unprivileged user to read root-owned files, potentially leading to privilege escalation. This flaw affects util-linux versions prior to 2.37.4.

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 1" src="https://img.shields.io/badge/L-1-fce1a9"/> <!-- unspecified: 0 --><strong>apt</strong> <code>2.2.4</code> (deb)</summary>

<small><code>pkg:deb/debian/apt@2.2.4?os_distro=bullseye&os_name=debian&os_version=11</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2011-3374?s=debian&n=apt&ns=debian&t=deb&osn=debian&osv=11&vr=%3E%3D2.2.4"><img alt="low : CVE--2011--3374" src="https://img.shields.io/badge/CVE--2011--3374-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.2.4</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.16%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>54th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

It was found that apt-key in apt, all versions, do not correctly validate gpg keys with the master keyring, leading to a potential man-in-the-middle attack.

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 1" src="https://img.shields.io/badge/L-1-fce1a9"/> <!-- unspecified: 0 --><strong>pcre2</strong> <code>10.36-2+deb11u1</code> (deb)</summary>

<small><code>pkg:deb/debian/pcre2@10.36-2%2Bdeb11u1?os_distro=bullseye&os_name=debian&os_version=11</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2022-41409?s=debian&n=pcre2&ns=debian&t=deb&osn=debian&osv=11&vr=%3E%3D10.36-2%2Bdeb11u1"><img alt="low : CVE--2022--41409" src="https://img.shields.io/badge/CVE--2022--41409-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=10.36-2+deb11u1</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.09%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>37th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

Integer overflow vulnerability in pcre2test before 10.41 allows attackers to cause a denial of service or other unspecified impacts via negative input.

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 1" src="https://img.shields.io/badge/L-1-fce1a9"/> <!-- unspecified: 0 --><strong>coreutils</strong> <code>8.32-4+b1</code> (deb)</summary>

<small><code>pkg:deb/debian/coreutils@8.32-4%2Bb1?os_distro=bullseye&os_name=debian&os_version=11</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2017-18018?s=debian&n=coreutils&ns=debian&t=deb&osn=debian&osv=11&vr=%3E%3D8.32-4"><img alt="low : CVE--2017--18018" src="https://img.shields.io/badge/CVE--2017--18018-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=8.32-4</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.04%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>5th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

In GNU Coreutils through 8.29, chown-core.c in chown and chgrp does not prevent replacement of a plain file with a symlink during use of the POSIX "-R -L" options, which allows local users to modify the ownership of arbitrary files by leveraging a race condition.

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 1" src="https://img.shields.io/badge/L-1-fce1a9"/> <!-- unspecified: 0 --><strong>tar</strong> <code>1.34+dfsg-1+deb11u1</code> (deb)</summary>

<small><code>pkg:deb/debian/tar@1.34%2Bdfsg-1%2Bdeb11u1?os_distro=bullseye&os_name=debian&os_version=11</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2005-2541?s=debian&n=tar&ns=debian&t=deb&osn=debian&osv=11&vr=%3E%3D1.34%2Bdfsg-1%2Bdeb11u1"><img alt="low : CVE--2005--2541" src="https://img.shields.io/badge/CVE--2005--2541-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=1.34+dfsg-1+deb11u1</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.69%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>81st percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

Tar 1.15.1 does not properly warn the user when extracting setuid or setgid files, which may allow local users or remote attackers to gain privileges.

</blockquote>
</details>
</details></td></tr>
</table>

