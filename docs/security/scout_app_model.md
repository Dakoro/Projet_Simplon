<h2>:mag: Vulnerabilities of <code>b7793f43e056:latest</code></h2>

<details open="true"><summary>:package: Image Reference</strong> <code>b7793f43e056:latest</code></summary>
<table>
<tr><td>digest</td><td><code>sha256:b7793f43e0566d48f35535847eea758058a803cf62431057eb24a04f7b110d12</code></td><tr><tr><td>vulnerabilities</td><td><img alt="critical: 2" src="https://img.shields.io/badge/critical-2-8b1924"/> <img alt="high: 6" src="https://img.shields.io/badge/high-6-e25d68"/> <img alt="medium: 5" src="https://img.shields.io/badge/medium-5-fbb552"/> <img alt="low: 116" src="https://img.shields.io/badge/low-116-fce1a9"/> <img alt="unspecified: 2" src="https://img.shields.io/badge/unspecified-2-lightgrey"/></td></tr>
<tr><td>size</td><td>4.0 GB</td></tr>
<tr><td>packages</td><td>743</td></tr>
</table>
</details></table>
</details>

<table>
<tr><td valign="top">
<details><summary><img alt="critical: 1" src="https://img.shields.io/badge/C-1-8b1924"/> <img alt="high: 2" src="https://img.shields.io/badge/H-2-e25d68"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 4" src="https://img.shields.io/badge/L-4-fce1a9"/> <!-- unspecified: 0 --><strong>git</strong> <code>1:2.39.2-1.1</code> (deb)</summary>

<small><code>pkg:deb/debian/git@1:2.39.2-1.1?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2024-32002?s=debian&n=git&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D1%3A2.39.2-1.1"><img alt="critical : CVE--2024--32002" src="https://img.shields.io/badge/CVE--2024--32002-lightgrey?label=critical%20&labelColor=8b1924"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=1:2.39.2-1.1</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.15%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>52nd percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

Git is a revision control system. Prior to versions 2.45.1, 2.44.1, 2.43.4, 2.42.2, 2.41.1, 2.40.2, and 2.39.4, repositories with submodules can be crafted in a way that exploits a bug in Git whereby it can be fooled into writing files not into the submodule's worktree but into a `.git/` directory. This allows writing a hook that will be executed while the clone operation is still running, giving the user no opportunity to inspect the code that is being executed. The problem has been patched in versions 2.45.1, 2.44.1, 2.43.4, 2.42.2, 2.41.1, 2.40.2, and 2.39.4. If symbolic link support is disabled in Git (e.g. via `git config --global core.symlinks false`), the described attack won't work. As always, it is best to avoid cloning repositories from untrusted sources.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2024-32004?s=debian&n=git&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D1%3A2.39.2-1.1"><img alt="high : CVE--2024--32004" src="https://img.shields.io/badge/CVE--2024--32004-lightgrey?label=high%20&labelColor=e25d68"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=1:2.39.2-1.1</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.04%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>11th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

Git is a revision control system. Prior to versions 2.45.1, 2.44.1, 2.43.4, 2.42.2, 2.41.1, 2.40.2, and 2.39.4, an attacker can prepare a local repository in such a way that, when cloned, will execute arbitrary code during the operation. The problem has been patched in versions 2.45.1, 2.44.1, 2.43.4, 2.42.2, 2.41.1, 2.40.2, and 2.39.4. As a workaround, avoid cloning repositories from untrusted sources.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2024-32465?s=debian&n=git&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D1%3A2.39.2-1.1"><img alt="high : CVE--2024--32465" src="https://img.shields.io/badge/CVE--2024--32465-lightgrey?label=high%20&labelColor=e25d68"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=1:2.39.2-1.1</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.04%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>11th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

Git is a revision control system. The Git project recommends to avoid working in untrusted repositories, and instead to clone it first with `git clone --no-local` to obtain a clean copy. Git has specific protections to make that a safe operation even with an untrusted source repository, but vulnerabilities allow those protections to be bypassed. In the context of cloning local repositories owned by other users, this vulnerability has been covered in CVE-2024-32004. But there are circumstances where the fixes for CVE-2024-32004 are not enough: For example, when obtaining a `.zip` file containing a full copy of a Git repository, it should not be trusted by default to be safe, as e.g. hooks could be configured to run within the context of that repository. The problem has been patched in versions 2.45.1, 2.44.1, 2.43.4, 2.42.2, 2.41.1, 2.40.2, and 2.39.4. As a workaround, avoid using Git in repositories that have been obtained via archives from untrusted sources.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2024-32021?s=debian&n=git&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D1%3A2.39.2-1.1"><img alt="low : CVE--2024--32021" src="https://img.shields.io/badge/CVE--2024--32021-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=1:2.39.2-1.1</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.04%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>16th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

Git is a revision control system. Prior to versions 2.45.1, 2.44.1, 2.43.4, 2.42.2, 2.41.1, 2.40.2, and 2.39.4, when cloning a local source repository that contains symlinks via the filesystem, Git may create hardlinks to arbitrary user-readable files on the same filesystem as the target repository in the `objects/` directory. Cloning a local repository over the filesystem may creating hardlinks to arbitrary user-owned files on the same filesystem in the target Git repository's `objects/` directory. When cloning a repository over the filesystem (without explicitly specifying the `file://` protocol or `--no-local`), the optimizations for local cloning will be used, which include attempting to hard link the object files instead of copying them. While the code includes checks against symbolic links in the source repository, which were added during the fix for CVE-2022-39253, these checks can still be raced because the hard link operation ultimately follows symlinks. If the object on the filesystem appears as a file during the check, and then a symlink during the operation, this will allow the adversary to bypass the check and create hardlinks in the destination objects directory to arbitrary, user-readable files. The problem has been patched in versions 2.45.1, 2.44.1, 2.43.4, 2.42.2, 2.41.1, 2.40.2, and 2.39.4.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2024-32020?s=debian&n=git&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D1%3A2.39.2-1.1"><img alt="low : CVE--2024--32020" src="https://img.shields.io/badge/CVE--2024--32020-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=1:2.39.2-1.1</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.04%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>16th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

Git is a revision control system. Prior to versions 2.45.1, 2.44.1, 2.43.4, 2.42.2, 2.41.1, 2.40.2, and 2.39.4, local clones may end up hardlinking files into the target repository's object database when source and target repository reside on the same disk. If the source repository is owned by a different user, then those hardlinked files may be rewritten at any point in time by the untrusted user. Cloning local repositories will cause Git to either copy or hardlink files of the source repository into the target repository. This significantly speeds up such local clones compared to doing a "proper" clone and saves both disk space and compute time. When cloning a repository located on the same disk that is owned by a different user than the current user we also end up creating such hardlinks. These files will continue to be owned and controlled by the potentially-untrusted user and can be rewritten by them at will in the future. The problem has been patched in versions 2.45.1, 2.44.1, 2.43.4, 2.42.2, 2.41.1, 2.40.2, and 2.39.4.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2022-24975?s=debian&n=git&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D1%3A2.39.2-1.1"><img alt="low : CVE--2022--24975" src="https://img.shields.io/badge/CVE--2022--24975-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=1:2.39.2-1.1</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.17%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>54th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

The --mirror documentation for Git through 2.35.1 does not mention the availability of deleted content, aka the "GitBleed" issue. This could present a security risk if information-disclosure auditing processes rely on a clone operation without the --mirror option. Note: This has been disputed by multiple 3rd parties who believe this is an intended feature of the git binary and does not pose a security risk.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2018-1000021?s=debian&n=git&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D1%3A2.39.2-1.1"><img alt="low : CVE--2018--1000021" src="https://img.shields.io/badge/CVE--2018--1000021-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=1:2.39.2-1.1</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.16%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>53rd percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

GIT version 2.15.1 and earlier contains a Input Validation Error vulnerability in Client that can result in problems including messing up terminal configuration to RCE. This attack appear to be exploitable via The user must interact with a malicious git server, (or have their traffic modified in a MITM attack).

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 1" src="https://img.shields.io/badge/C-1-8b1924"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 0" src="https://img.shields.io/badge/L-0-lightgrey"/> <!-- unspecified: 0 --><strong>aom</strong> <code>3.6.0-1</code> (deb)</summary>

<small><code>pkg:deb/debian/aom@3.6.0-1?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2024-5171?s=debian&n=aom&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D3.6.0-1"><img alt="critical : CVE--2024--5171" src="https://img.shields.io/badge/CVE--2024--5171-lightgrey?label=critical%20&labelColor=8b1924"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=3.6.0-1</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.06%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>26th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

Integer overflow in libaom internal function img_alloc_helper can lead to heap buffer overflow. This function can be reached via 3 callers:     *  Calling aom_img_alloc() with a large value of the d_w, d_h, or align parameter may result in integer overflows in the calculations of buffer sizes and offsets and some fields of the returned aom_image_t struct may be invalid.   *  Calling aom_img_wrap() with a large value of the d_w, d_h, or align parameter may result in integer overflows in the calculations of buffer sizes and offsets and some fields of the returned aom_image_t struct may be invalid.   *  Calling aom_img_alloc_with_border() with a large value of the d_w, d_h, align, size_align, or border parameter may result in integer overflows in the calculations of buffer sizes and offsets and some fields of the returned aom_image_t struct may be invalid.

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 1" src="https://img.shields.io/badge/H-1-e25d68"/> <img alt="medium: 1" src="https://img.shields.io/badge/M-1-fbb552"/> <img alt="low: 0" src="https://img.shields.io/badge/L-0-lightgrey"/> <!-- unspecified: 0 --><strong>pip</strong> <code>23.0.1</code> (pypi)</summary>

<small><code>pkg:pypi/pip@23.0.1</code></small><br/>
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

<a href="https://scout.docker.com/v/CVE-2023-5752?s=github&n=pip&t=pypi&vr=%3C23.3"><img alt="medium 5.5: CVE--2023--5752" src="https://img.shields.io/badge/CVE--2023--5752-lightgrey?label=medium%205.5&labelColor=fbb552"/></a> <i>Improper Neutralization of Special Elements used in a Command ('Command Injection')</i>

<table>
<tr><td>Affected range</td><td><code><23.3</code></td></tr>
<tr><td>Fixed version</td><td><code>23.3</code></td></tr>
<tr><td>CVSS Score</td><td><code>5.5</code></td></tr>
<tr><td>CVSS Vector</td><td><code>CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:H/A:N</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.04%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>16th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

When installing a package from a Mercurial VCS URL, e.g. `pip install hg+...`, with pip prior to v23.3, the specified Mercurial revision could be used to inject arbitrary configuration options to the `hg clone` call (e.g. `--config`). Controlling the Mercurial configuration can modify how and which repository is installed. This vulnerability does not affect users who aren't installing from Mercurial.

</blockquote>
</details>
</details></td></tr>

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
<tr><td>EPSS Percentile</td><td><code>9th percentile</code></td></tr>
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
<tr><td>EPSS Percentile</td><td><code>9th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

python-jose through 3.3.0 allows attackers to cause a denial of service (resource consumption) during a decode via a crafted JSON Web Encryption (JWE) token with a high compression ratio, aka a "JWT bomb." This is similar to CVE-2024-21319.

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 1" src="https://img.shields.io/badge/H-1-e25d68"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 0" src="https://img.shields.io/badge/L-0-lightgrey"/> <!-- unspecified: 0 --><strong>nltk</strong> <code>3.8.1</code> (pypi)</summary>

<small><code>pkg:pypi/nltk@3.8.1</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2024-39705?s=github&n=nltk&t=pypi&vr=%3C%3D3.8.1"><img alt="high 7.5: CVE--2024--39705" src="https://img.shields.io/badge/CVE--2024--39705-lightgrey?label=high%207.5&labelColor=e25d68"/></a> <i>Channel Accessible by Non-Endpoint</i>

<table>
<tr><td>Affected range</td><td><code><=3.8.1</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>CVSS Score</td><td><code>7.5</code></td></tr>
<tr><td>CVSS Vector</td><td><code>CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.04%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>9th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

NLTK through 3.8.1 allows remote code execution if untrusted packages have pickled Python code, and the integrated data package download functionality is used. This affects, for example, averaged_perceptron_tagger and punkt.

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
<tr><td>EPSS Percentile</td><td><code>9th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A vulnerability in the `package_index` module of pypa/setuptools versions up to 69.1.1 allows for remote code execution via its download functions. These functions, which are used to download packages from URLs provided by users or retrieved from package index servers, are susceptible to code injection. If these functions are exposed to user-controlled inputs, such as package URLs, they can execute arbitrary commands on the system. The issue is fixed in version 70.0.

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 2" src="https://img.shields.io/badge/M-2-fbb552"/> <img alt="low: 2" src="https://img.shields.io/badge/L-2-fce1a9"/> <!-- unspecified: 0 --><strong>libwmf</strong> <code>0.2.12-5.1</code> (deb)</summary>

<small><code>pkg:deb/debian/libwmf@0.2.12-5.1?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2009-3546?s=debian&n=libwmf&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D0.2.12-5.1"><img alt="medium : CVE--2009--3546" src="https://img.shields.io/badge/CVE--2009--3546-lightgrey?label=medium%20&labelColor=fbb552"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=0.2.12-5.1</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>1.81%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>88th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

The _gdGetColors function in gd_gd.c in PHP 5.2.11 and 5.3.x before 5.3.1, and the GD Graphics Library 2.x, does not properly verify a certain colorsTotal structure member, which might allow remote attackers to conduct buffer overflow or buffer over-read attacks via a crafted GD file, a different vulnerability than CVE-2009-3293. NOTE: some of these details are obtained from third party information.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2007-3996?s=debian&n=libwmf&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D0.2.12-5.1"><img alt="medium : CVE--2007--3996" src="https://img.shields.io/badge/CVE--2007--3996-lightgrey?label=medium%20&labelColor=fbb552"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=0.2.12-5.1</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>2.76%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>91st percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

Multiple integer overflows in libgd in PHP before 5.2.4 allow remote attackers to cause a denial of service (application crash) and possibly execute arbitrary code via a large (1) srcW or (2) srcH value to the (a) gdImageCopyResized function, or a large (3) sy (height) or (4) sx (width) value to the (b) gdImageCreate or the (c) gdImageCreateTrueColor function.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2007-3477?s=debian&n=libwmf&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D0.2.12-5.1"><img alt="low : CVE--2007--3477" src="https://img.shields.io/badge/CVE--2007--3477-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=0.2.12-5.1</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>2.91%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>91st percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

The (a) imagearc and (b) imagefilledarc functions in GD Graphics Library (libgd) before 2.0.35 allow attackers to cause a denial of service (CPU consumption) via a large (1) start or (2) end angle degree value.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2007-3476?s=debian&n=libwmf&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D0.2.12-5.1"><img alt="low : CVE--2007--3476" src="https://img.shields.io/badge/CVE--2007--3476-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=0.2.12-5.1</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>2.73%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>91st percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

Array index error in gd_gif_in.c in the GD Graphics Library (libgd) before 2.0.35 allows user-assisted remote attackers to cause a denial of service (crash and heap corruption) via large color index values in crafted image data, which results in a segmentation fault.

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 1" src="https://img.shields.io/badge/M-1-fbb552"/> <img alt="low: 0" src="https://img.shields.io/badge/L-0-lightgrey"/> <!-- unspecified: 0 --><strong>nghttp2</strong> <code>1.52.0-1+deb12u1</code> (deb)</summary>

<small><code>pkg:deb/debian/nghttp2@1.52.0-1%2Bdeb12u1?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2024-28182?s=debian&n=nghttp2&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D1.52.0-1%2Bdeb12u1"><img alt="medium : CVE--2024--28182" src="https://img.shields.io/badge/CVE--2024--28182-lightgrey?label=medium%20&labelColor=fbb552"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=1.52.0-1+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.04%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>14th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

nghttp2 is an implementation of the Hypertext Transfer Protocol version 2 in C. The nghttp2 library prior to version 1.61.0 keeps reading the unbounded number of HTTP/2 CONTINUATION frames even after a stream is reset to keep HPACK context in sync.  This causes excessive CPU usage to decode HPACK stream. nghttp2 v1.61.0 mitigates this vulnerability by limiting the number of CONTINUATION frames it accepts per stream. There is no workaround for this vulnerability.

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 13" src="https://img.shields.io/badge/L-13-fce1a9"/> <!-- unspecified: 0 --><strong>openjpeg2</strong> <code>2.5.0-2</code> (deb)</summary>

<small><code>pkg:deb/debian/openjpeg2@2.5.0-2?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2018-20846?s=debian&n=openjpeg2&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.5.0-2"><img alt="low : CVE--2018--20846" src="https://img.shields.io/badge/CVE--2018--20846-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.5.0-2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.15%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>51st percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

Out-of-bounds accesses in the functions pi_next_lrcp, pi_next_rlcp, pi_next_rpcl, pi_next_pcrl, pi_next_rpcl, and pi_next_cprl in openmj2/pi.c in OpenJPEG through 2.3.0 allow remote attackers to cause a denial of service (application crash).

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2018-16376?s=debian&n=openjpeg2&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.5.0-2"><img alt="low : CVE--2018--16376" src="https://img.shields.io/badge/CVE--2018--16376-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.5.0-2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.31%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>70th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

An issue was discovered in OpenJPEG 2.3.0. A heap-based buffer overflow was discovered in the function t2_encode_packet in lib/openmj2/t2.c. The vulnerability causes an out-of-bounds write, which may lead to remote denial of service or possibly unspecified other impact.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2018-16375?s=debian&n=openjpeg2&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.5.0-2"><img alt="low : CVE--2018--16375" src="https://img.shields.io/badge/CVE--2018--16375-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.5.0-2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.23%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>62nd percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

An issue was discovered in OpenJPEG 2.3.0. Missing checks for header_info.height and header_info.width in the function pnmtoimage in bin/jpwl/convert.c can lead to a heap-based buffer overflow.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2017-17479?s=debian&n=openjpeg2&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.5.0-2"><img alt="low : CVE--2017--17479" src="https://img.shields.io/badge/CVE--2017--17479-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.5.0-2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>1.60%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>88th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

In OpenJPEG 2.3.0, a stack-based buffer overflow was discovered in the pgxtoimage function in jpwl/convert.c. The vulnerability causes an out-of-bounds write, which may lead to remote denial of service or possibly remote code execution.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2016-9581?s=debian&n=openjpeg2&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.5.0-2"><img alt="low : CVE--2016--9581" src="https://img.shields.io/badge/CVE--2016--9581-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.5.0-2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.57%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>78th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

An infinite loop vulnerability in tiftoimage that results in heap buffer overflow in convert_32s_C1P1 was found in openjpeg 2.1.2.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2016-9580?s=debian&n=openjpeg2&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.5.0-2"><img alt="low : CVE--2016--9580" src="https://img.shields.io/badge/CVE--2016--9580-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.5.0-2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.49%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>76th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

An integer overflow vulnerability was found in tiftoimage function in openjpeg 2.1.2, resulting in heap buffer overflow.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2016-9117?s=debian&n=openjpeg2&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.5.0-2"><img alt="low : CVE--2016--9117" src="https://img.shields.io/badge/CVE--2016--9117-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.5.0-2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.10%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>42nd percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

NULL Pointer Access in function imagetopnm of convert.c(jp2):1289 in OpenJPEG 2.1.2. Impact is Denial of Service. Someone must open a crafted j2k file.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2016-9116?s=debian&n=openjpeg2&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.5.0-2"><img alt="low : CVE--2016--9116" src="https://img.shields.io/badge/CVE--2016--9116-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.5.0-2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.10%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>42nd percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

NULL Pointer Access in function imagetopnm of convert.c:2226(jp2) in OpenJPEG 2.1.2. Impact is Denial of Service. Someone must open a crafted j2k file.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2016-9115?s=debian&n=openjpeg2&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.5.0-2"><img alt="low : CVE--2016--9115" src="https://img.shields.io/badge/CVE--2016--9115-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.5.0-2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.14%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>51st percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

Heap Buffer Over-read in function imagetotga of convert.c(jp2):942 in OpenJPEG 2.1.2. Impact is Denial of Service. Someone must open a crafted j2k file.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2016-9114?s=debian&n=openjpeg2&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.5.0-2"><img alt="low : CVE--2016--9114" src="https://img.shields.io/badge/CVE--2016--9114-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.5.0-2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.36%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>72nd percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

There is a NULL Pointer Access in function imagetopnm of convert.c:1943(jp2) of OpenJPEG 2.1.2. image->comps[compno].data is not assigned a value after initialization(NULL). Impact is Denial of Service.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2016-9113?s=debian&n=openjpeg2&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.5.0-2"><img alt="low : CVE--2016--9113" src="https://img.shields.io/badge/CVE--2016--9113-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.5.0-2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.36%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>72nd percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

There is a NULL pointer dereference in function imagetobmp of convertbmp.c:980 of OpenJPEG 2.1.2. image->comps[0].data is not assigned a value after initialization(NULL). Impact is Denial of Service.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2016-10506?s=debian&n=openjpeg2&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.5.0-2"><img alt="low : CVE--2016--10506" src="https://img.shields.io/badge/CVE--2016--10506-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.5.0-2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>1.01%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>84th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

Division-by-zero vulnerabilities in the functions opj_pi_next_cprl, opj_pi_next_pcrl, and opj_pi_next_rpcl in pi.c in OpenJPEG before 2.2.0 allow remote attackers to cause a denial of service (application crash) via crafted j2k files.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2016-10505?s=debian&n=openjpeg2&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.5.0-2"><img alt="low : CVE--2016--10505" src="https://img.shields.io/badge/CVE--2016--10505-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.5.0-2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.58%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>78th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

NULL pointer dereference vulnerabilities in the imagetopnm function in convert.c, sycc444_to_rgb function in color.c, color_esycc_to_rgb function in color.c, and sycc422_to_rgb function in color.c in OpenJPEG before 2.2.0 allow remote attackers to cause a denial of service (application crash) via crafted j2k files.

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 10" src="https://img.shields.io/badge/L-10-fce1a9"/> <!-- unspecified: 0 --><strong>bluez</strong> <code>5.66-1+deb12u2</code> (deb)</summary>

<small><code>pkg:deb/debian/bluez@5.66-1%2Bdeb12u2?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2016-9918?s=debian&n=bluez&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D5.66-1%2Bdeb12u2"><img alt="low : CVE--2016--9918" src="https://img.shields.io/badge/CVE--2016--9918-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=5.66-1+deb12u2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.30%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>70th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

In BlueZ 5.42, an out-of-bounds read was identified in "packet_hexdump" function in "monitor/packet.c" source file. This issue can be triggered by processing a corrupted dump file and will result in btmon crash.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2016-9917?s=debian&n=bluez&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D5.66-1%2Bdeb12u2"><img alt="low : CVE--2016--9917" src="https://img.shields.io/badge/CVE--2016--9917-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=5.66-1+deb12u2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.14%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>50th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

In BlueZ 5.42, a buffer overflow was observed in "read_n" function in "tools/hcidump.c" source file. This issue can be triggered by processing a corrupted dump file and will result in hcidump crash.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2016-9804?s=debian&n=bluez&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D5.66-1%2Bdeb12u2"><img alt="low : CVE--2016--9804" src="https://img.shields.io/badge/CVE--2016--9804-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=5.66-1+deb12u2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.20%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>58th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

In BlueZ 5.42, a buffer overflow was observed in "commands_dump" function in "tools/parser/csr.c" source file. The issue exists because "commands" array is overflowed by supplied parameter due to lack of boundary checks on size of the buffer from frame "frm->ptr" parameter. This issue can be triggered by processing a corrupted dump file and will result in hcidump crash.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2016-9803?s=debian&n=bluez&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D5.66-1%2Bdeb12u2"><img alt="low : CVE--2016--9803" src="https://img.shields.io/badge/CVE--2016--9803-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=5.66-1+deb12u2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.20%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>58th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

In BlueZ 5.42, an out-of-bounds read was observed in "le_meta_ev_dump" function in "tools/parser/hci.c" source file. This issue exists because 'subevent' (which is used to read correct element from 'ev_le_meta_str' array) is overflowed.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2016-9802?s=debian&n=bluez&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D5.66-1%2Bdeb12u2"><img alt="low : CVE--2016--9802" src="https://img.shields.io/badge/CVE--2016--9802-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=5.66-1+deb12u2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.31%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>70th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

In BlueZ 5.42, a buffer over-read was identified in "l2cap_packet" function in "monitor/packet.c" source file. This issue can be triggered by processing a corrupted dump file and will result in btmon crash.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2016-9801?s=debian&n=bluez&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D5.66-1%2Bdeb12u2"><img alt="low : CVE--2016--9801" src="https://img.shields.io/badge/CVE--2016--9801-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=5.66-1+deb12u2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.20%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>58th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

In BlueZ 5.42, a buffer overflow was observed in "set_ext_ctrl" function in "tools/parser/l2cap.c" source file when processing corrupted dump file.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2016-9800?s=debian&n=bluez&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D5.66-1%2Bdeb12u2"><img alt="low : CVE--2016--9800" src="https://img.shields.io/badge/CVE--2016--9800-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=5.66-1+deb12u2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.20%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>58th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

In BlueZ 5.42, a buffer overflow was observed in "pin_code_reply_dump" function in "tools/parser/hci.c" source file. The issue exists because "pin" array is overflowed by supplied parameter due to lack of boundary checks on size of the buffer from frame "pin_code_reply_cp *cp" parameter.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2016-9799?s=debian&n=bluez&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D5.66-1%2Bdeb12u2"><img alt="low : CVE--2016--9799" src="https://img.shields.io/badge/CVE--2016--9799-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=5.66-1+deb12u2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.20%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>58th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

In BlueZ 5.42, a buffer overflow was observed in "pklg_read_hci" function in "btsnoop.c" source file. This issue can be triggered by processing a corrupted dump file and will result in btmon crash.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2016-9798?s=debian&n=bluez&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D5.66-1%2Bdeb12u2"><img alt="low : CVE--2016--9798" src="https://img.shields.io/badge/CVE--2016--9798-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=5.66-1+deb12u2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.37%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>73rd percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

In BlueZ 5.42, a use-after-free was identified in "conf_opt" function in "tools/parser/l2cap.c" source file. This issue can be triggered by processing a corrupted dump file and will result in hcidump crash.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2016-9797?s=debian&n=bluez&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D5.66-1%2Bdeb12u2"><img alt="low : CVE--2016--9797" src="https://img.shields.io/badge/CVE--2016--9797-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=5.66-1+deb12u2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.22%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>60th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

In BlueZ 5.42, a buffer over-read was observed in "l2cap_dump" function in "tools/parser/l2cap.c" source file. This issue can be triggered by processing a corrupted dump file and will result in hcidump crash.

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 10" src="https://img.shields.io/badge/L-10-fce1a9"/> <!-- unspecified: 0 --><strong>tiff</strong> <code>4.5.0-6+deb12u1</code> (deb)</summary>

<small><code>pkg:deb/debian/tiff@4.5.0-6%2Bdeb12u1?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2024-6716?s=debian&n=tiff&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D4.5.0-6%2Bdeb12u1"><img alt="low : CVE--2024--6716" src="https://img.shields.io/badge/CVE--2024--6716-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=4.5.0-6+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.04%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>16th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A flaw was found in the libtiff library. An out-of-memory issue in the TIFFReadEncodedStrip function can be triggered when processing a crafted TIFF file, allowing attackers to perform memory allocation of arbitrary sizes, resulting in a denial of service.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2023-6228?s=debian&n=tiff&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D4.5.0-6%2Bdeb12u1"><img alt="low : CVE--2023--6228" src="https://img.shields.io/badge/CVE--2023--6228-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=4.5.0-6+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.04%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>11th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

An issue was found in the tiffcp utility distributed by the libtiff package where a crafted TIFF file on processing may cause a heap-based buffer overflow leads to an application crash.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2023-3164?s=debian&n=tiff&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D4.5.0-6%2Bdeb12u1"><img alt="low : CVE--2023--3164" src="https://img.shields.io/badge/CVE--2023--3164-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=4.5.0-6+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.04%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>11th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A heap-buffer-overflow vulnerability was found in LibTIFF, in extractImageSection() at tools/tiffcrop.c:7916 and tools/tiffcrop.c:7801. This flaw allows attackers to cause a denial of service via a crafted tiff file.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2023-1916?s=debian&n=tiff&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D4.5.0-6%2Bdeb12u1"><img alt="low : CVE--2023--1916" src="https://img.shields.io/badge/CVE--2023--1916-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=4.5.0-6+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.05%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>19th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A flaw was found in tiffcrop, a program distributed by the libtiff package. A specially crafted tiff file can lead to an out-of-bounds read in the extractImageSection function in tools/tiffcrop.c, resulting in a denial of service and limited information disclosure. This issue affects libtiff versions 4.x.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2022-1210?s=debian&n=tiff&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D4.5.0-6%2Bdeb12u1"><img alt="low : CVE--2022--1210" src="https://img.shields.io/badge/CVE--2022--1210-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=4.5.0-6+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.33%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>72nd percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A vulnerability classified as problematic was found in LibTIFF 4.3.0. Affected by this vulnerability is the TIFF File Handler of tiff2ps. Opening a malicious file leads to a denial of service. The attack can be launched remotely but requires user interaction. The exploit has been disclosed to the public and may be used.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2018-10126?s=debian&n=tiff&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D4.5.0-6%2Bdeb12u1"><img alt="low : CVE--2018--10126" src="https://img.shields.io/badge/CVE--2018--10126-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=4.5.0-6+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.10%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>42nd percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

LibTIFF 4.0.9 has a NULL pointer dereference in the jpeg_fdct_16x16 function in jfdctint.c.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2017-9117?s=debian&n=tiff&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D4.5.0-6%2Bdeb12u1"><img alt="low : CVE--2017--9117" src="https://img.shields.io/badge/CVE--2017--9117-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=4.5.0-6+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.62%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>79th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

In LibTIFF 4.0.7, the program processes BMP images without verifying that biWidth and biHeight in the bitmap-information header match the actual input, leading to a heap-based buffer over-read in bmp2tiff.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2017-5563?s=debian&n=tiff&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D4.5.0-6%2Bdeb12u1"><img alt="low : CVE--2017--5563" src="https://img.shields.io/badge/CVE--2017--5563-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=4.5.0-6+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.54%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>77th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

LibTIFF version 4.0.7 is vulnerable to a heap-based buffer over-read in tif_lzw.c resulting in DoS or code execution via a crafted bmp image to tools/bmp2tiff.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2017-17973?s=debian&n=tiff&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D4.5.0-6%2Bdeb12u1"><img alt="low : CVE--2017--17973" src="https://img.shields.io/badge/CVE--2017--17973-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=4.5.0-6+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.48%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>76th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

In LibTIFF 4.0.8, there is a heap-based use-after-free in the t2p_writeproc function in tiff2pdf.c. NOTE: there is a third-party report of inability to reproduce this issue

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2017-16232?s=debian&n=tiff&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D4.5.0-6%2Bdeb12u1"><img alt="low : CVE--2017--16232" src="https://img.shields.io/badge/CVE--2017--16232-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=4.5.0-6+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>1.73%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>88th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

LibTIFF 4.0.8 has multiple memory leak vulnerabilities, which allow attackers to cause a denial of service (memory consumption), as demonstrated by tif_open.c, tif_lzw.c, and tif_aux.c. NOTE: Third parties were unable to reproduce the issue

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 9" src="https://img.shields.io/badge/L-9-fce1a9"/> <!-- unspecified: 0 --><strong>openssh</strong> <code>1:9.2p1-2+deb12u3</code> (deb)</summary>

<small><code>pkg:deb/debian/openssh@1:9.2p1-2%2Bdeb12u3?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2023-51767?s=debian&n=openssh&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D1%3A9.2p1-2%2Bdeb12u2"><img alt="low : CVE--2023--51767" src="https://img.shields.io/badge/CVE--2023--51767-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=1:9.2p1-2+deb12u2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.05%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>21st percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

OpenSSH through 9.6, when common types of DRAM are used, might allow row hammer attacks (for authentication bypass) because the integer value of authenticated in mm_answer_authpassword does not resist flips of a single bit. NOTE: this is applicable to a certain threat model of attacker-victim co-location in which the attacker has user privileges.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2020-15778?s=debian&n=openssh&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D1%3A9.2p1-2%2Bdeb12u2"><img alt="low : CVE--2020--15778" src="https://img.shields.io/badge/CVE--2020--15778-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=1:9.2p1-2+deb12u2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.42%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>74th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

scp in OpenSSH through 8.3p1 allows command injection in the scp.c toremote function, as demonstrated by backtick characters in the destination argument. NOTE: the vendor reportedly has stated that they intentionally omit validation of "anomalous argument transfers" because that could "stand a great chance of breaking existing workflows."

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2020-14145?s=debian&n=openssh&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D1%3A9.2p1-2%2Bdeb12u2"><img alt="low : CVE--2020--14145" src="https://img.shields.io/badge/CVE--2020--14145-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=1:9.2p1-2+deb12u2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.33%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>71st percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

The client side in OpenSSH 5.7 through 8.4 has an Observable Discrepancy leading to an information leak in the algorithm negotiation. This allows man-in-the-middle attackers to target initial connection attempts (where no host key for the server has been cached by the client). NOTE: some reports state that 8.5 and 8.6 are also affected.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2019-6110?s=debian&n=openssh&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D1%3A9.2p1-2%2Bdeb12u2"><img alt="low : CVE--2019--6110" src="https://img.shields.io/badge/CVE--2019--6110-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=1:9.2p1-2+deb12u2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.42%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>74th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

In OpenSSH 7.9, due to accepting and displaying arbitrary stderr output from the server, a malicious server (or Man-in-The-Middle attacker) can manipulate the client output, for example to use ANSI control codes to hide additional files being transferred.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2018-15919?s=debian&n=openssh&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D1%3A9.2p1-2%2Bdeb12u2"><img alt="low : CVE--2018--15919" src="https://img.shields.io/badge/CVE--2018--15919-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=1:9.2p1-2+deb12u2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.26%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>66th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

Remotely observable behaviour in auth-gss2.c in OpenSSH through 7.8 could be used by remote attackers to detect existence of users on a target system when GSS2 is in use. NOTE: the discoverer states 'We understand that the OpenSSH developers do not want to treat such a username enumeration (or "oracle") as a vulnerability.'

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2016-20012?s=debian&n=openssh&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D1%3A9.2p1-2%2Bdeb12u2"><img alt="low : CVE--2016--20012" src="https://img.shields.io/badge/CVE--2016--20012-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=1:9.2p1-2+deb12u2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.59%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>78th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

OpenSSH through 8.7 allows remote attackers, who have a suspicion that a certain combination of username and public key is known to an SSH server, to test whether this suspicion is correct. This occurs because a challenge is sent only when that combination could be valid for a login session. NOTE: the vendor does not recognize user enumeration as a vulnerability for this product

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2008-3234?s=debian&n=openssh&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D1%3A9.2p1-2%2Bdeb12u2"><img alt="low : CVE--2008--3234" src="https://img.shields.io/badge/CVE--2008--3234-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=1:9.2p1-2+deb12u2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>1.15%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>85th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

sshd in OpenSSH 4 on Debian GNU/Linux, and the 20070303 OpenSSH snapshot, allows remote authenticated users to obtain access to arbitrary SELinux roles by appending a :/ (colon slash) sequence, followed by the role name, to the username.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2007-2768?s=debian&n=openssh&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D1%3A9.2p1-2%2Bdeb12u2"><img alt="low : CVE--2007--2768" src="https://img.shields.io/badge/CVE--2007--2768-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=1:9.2p1-2+deb12u2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.26%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>66th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

OpenSSH, when using OPIE (One-Time Passwords in Everything) for PAM, allows remote attackers to determine the existence of certain user accounts, which displays a different response if the user account exists and is configured to use one-time passwords (OTP), a similar issue to CVE-2007-2243.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2007-2243?s=debian&n=openssh&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D1%3A9.2p1-2%2Bdeb12u2"><img alt="low : CVE--2007--2243" src="https://img.shields.io/badge/CVE--2007--2243-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=1:9.2p1-2+deb12u2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.72%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>81st percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

OpenSSH 4.6 and earlier, when ChallengeResponseAuthentication is enabled, allows remote attackers to determine the existence of user accounts by attempting to authenticate via S/KEY, which displays a different response if the user account exists, a similar issue to CVE-2001-1483.

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 9" src="https://img.shields.io/badge/L-9-fce1a9"/> <!-- unspecified: 0 --><strong>imagemagick</strong> <code>8:6.9.11.60+dfsg-1.6+deb12u1</code> (deb)</summary>

<small><code>pkg:deb/debian/imagemagick@8:6.9.11.60%2Bdfsg-1.6%2Bdeb12u1?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2023-34152?s=debian&n=imagemagick&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D8%3A6.9.11.60%2Bdfsg-1.6%2Bdeb12u1"><img alt="low : CVE--2023--34152" src="https://img.shields.io/badge/CVE--2023--34152-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=8:6.9.11.60+dfsg-1.6+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.53%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>77th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A vulnerability was found in ImageMagick. This security flaw cause a remote code execution vulnerability in OpenBlob with --enable-pipes configured.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2021-20311?s=debian&n=imagemagick&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D8%3A6.9.11.60%2Bdfsg-1.6%2Bdeb12u1"><img alt="low : CVE--2021--20311" src="https://img.shields.io/badge/CVE--2021--20311-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=8:6.9.11.60+dfsg-1.6+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.09%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>37th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A flaw was found in ImageMagick in versions before 7.0.11, where a division by zero in sRGBTransformImage() in the MagickCore/colorspace.c may trigger undefined behavior via a crafted image file that is submitted by an attacker processed by an application using ImageMagick. The highest threat from this vulnerability is to system availability.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2018-15607?s=debian&n=imagemagick&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D8%3A6.9.11.60%2Bdfsg-1.6%2Bdeb12u1"><img alt="low : CVE--2018--15607" src="https://img.shields.io/badge/CVE--2018--15607-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=8:6.9.11.60+dfsg-1.6+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.21%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>59th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

In ImageMagick 7.0.8-11 Q16, a tiny input file 0x50 0x36 0x36 0x36 0x36 0x4c 0x36 0x38 0x36 0x36 0x36 0x36 0x36 0x36 0x1f 0x35 0x50 0x00 can result in a hang of several minutes during which CPU and memory resources are consumed until ultimately an attempted large memory allocation fails. Remote attackers could leverage this vulnerability to cause a denial of service via a crafted file.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2017-7275?s=debian&n=imagemagick&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D8%3A6.9.11.60%2Bdfsg-1.6%2Bdeb12u1"><img alt="low : CVE--2017--7275" src="https://img.shields.io/badge/CVE--2017--7275-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=8:6.9.11.60+dfsg-1.6+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.24%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>62nd percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

The ReadPCXImage function in coders/pcx.c in ImageMagick 7.0.4.9 allows remote attackers to cause a denial of service (attempted large memory allocation and application crash) via a crafted file. NOTE: this vulnerability exists because of an incomplete fix for CVE-2016-8862 and CVE-2016-8866.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2017-11755?s=debian&n=imagemagick&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D8%3A6.9.11.60%2Bdfsg-1.6%2Bdeb12u1"><img alt="low : CVE--2017--11755" src="https://img.shields.io/badge/CVE--2017--11755-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=8:6.9.11.60+dfsg-1.6+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.14%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>50th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

The WritePICONImage function in coders/xpm.c in ImageMagick 7.0.6-4 allows remote attackers to cause a denial of service (memory leak) via a crafted file that is mishandled in an AcquireSemaphoreInfo call.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2017-11754?s=debian&n=imagemagick&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D8%3A6.9.11.60%2Bdfsg-1.6%2Bdeb12u1"><img alt="low : CVE--2017--11754" src="https://img.shields.io/badge/CVE--2017--11754-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=8:6.9.11.60+dfsg-1.6+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.14%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>50th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

The WritePICONImage function in coders/xpm.c in ImageMagick 7.0.6-4 allows remote attackers to cause a denial of service (memory leak) via a crafted file that is mishandled in an OpenPixelCache call.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2016-8678?s=debian&n=imagemagick&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D8%3A6.9.11.60%2Bdfsg-1.6%2Bdeb12u1"><img alt="low : CVE--2016--8678" src="https://img.shields.io/badge/CVE--2016--8678-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=8:6.9.11.60+dfsg-1.6+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.53%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>77th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

The IsPixelMonochrome function in MagickCore/pixel-accessor.h in ImageMagick 7.0.3.0 allows remote attackers to cause a denial of service (out-of-bounds read and crash) via a crafted file.  NOTE: the vendor says "This is a Q64 issue and we do not support Q64."

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2008-3134?s=debian&n=imagemagick&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D8%3A6.9.11.60%2Bdfsg-1.6%2Bdeb12u1"><img alt="low : CVE--2008--3134" src="https://img.shields.io/badge/CVE--2008--3134-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=8:6.9.11.60+dfsg-1.6+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>5.76%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>93rd percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

Multiple unspecified vulnerabilities in GraphicsMagick before 1.2.4 allow remote attackers to cause a denial of service (crash, infinite loop, or memory consumption) via (a) unspecified vectors in the (1) AVI, (2) AVS, (3) DCM, (4) EPT, (5) FITS, (6) MTV, (7) PALM, (8) RLA, and (9) TGA decoder readers; and (b) the GetImageCharacteristics function in magick/image.c, as reachable from a crafted (10) PNG, (11) JPEG, (12) BMP, or (13) TIFF file.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2005-0406?s=debian&n=imagemagick&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D8%3A6.9.11.60%2Bdfsg-1.6%2Bdeb12u1"><img alt="low : CVE--2005--0406" src="https://img.shields.io/badge/CVE--2005--0406-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=8:6.9.11.60+dfsg-1.6+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.05%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>17th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A design flaw in image processing software that modifies JPEG images might not modify the original EXIF thumbnail, which could lead to an information leak of potentially sensitive visual information that had been removed from the main JPEG image.

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 7" src="https://img.shields.io/badge/L-7-fce1a9"/> <!-- unspecified: 0 --><strong>binutils</strong> <code>2.40-2</code> (deb)</summary>

<small><code>pkg:deb/debian/binutils@2.40-2?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2023-1972?s=debian&n=binutils&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.40-2"><img alt="low : CVE--2023--1972" src="https://img.shields.io/badge/CVE--2023--1972-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.40-2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.08%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>34th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A potential heap based buffer overflow was found in _bfd_elf_slurp_version_tables() in bfd/elf.c. This may lead to loss of availability.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2021-32256?s=debian&n=binutils&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.40-2"><img alt="low : CVE--2021--32256" src="https://img.shields.io/badge/CVE--2021--32256-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.40-2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.06%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>28th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

An issue was discovered in GNU libiberty, as distributed in GNU Binutils 2.36. It is a stack-overflow issue in demangle_type in rust-demangle.c.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2018-9996?s=debian&n=binutils&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.40-2"><img alt="low : CVE--2018--9996" src="https://img.shields.io/badge/CVE--2018--9996-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.40-2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.05%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>19th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

An issue was discovered in cplus-dem.c in GNU libiberty, as distributed in GNU Binutils 2.30. Stack Exhaustion occurs in the C++ demangling functions provided by libiberty, and there are recursive stack frames: demangle_template_value_parm, demangle_integral_value, and demangle_expression.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2018-20712?s=debian&n=binutils&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.40-2"><img alt="low : CVE--2018--20712" src="https://img.shields.io/badge/CVE--2018--20712-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.40-2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.11%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>45th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A heap-based buffer over-read exists in the function d_expression_1 in cp-demangle.c in GNU libiberty, as distributed in GNU Binutils 2.31.1. A crafted input can cause segmentation faults, leading to denial-of-service, as demonstrated by c++filt.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2018-20673?s=debian&n=binutils&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.40-2"><img alt="low : CVE--2018--20673" src="https://img.shields.io/badge/CVE--2018--20673-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.40-2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.04%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>16th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

The demangle_template function in cplus-dem.c in GNU libiberty, as distributed in GNU Binutils 2.31.1, contains an integer overflow vulnerability (for "Create an array for saving the template argument values") that can trigger a heap-based buffer overflow, as demonstrated by nm.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2018-18483?s=debian&n=binutils&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.40-2"><img alt="low : CVE--2018--18483" src="https://img.shields.io/badge/CVE--2018--18483-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.40-2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.99%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>84th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

The get_count function in cplus-dem.c in GNU libiberty, as distributed in GNU Binutils 2.31, allows remote attackers to cause a denial of service (malloc called with the result of an integer-overflowing calculation) or possibly have unspecified other impact via a crafted string, as demonstrated by c++filt.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2017-13716?s=debian&n=binutils&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.40-2"><img alt="low : CVE--2017--13716" src="https://img.shields.io/badge/CVE--2017--13716-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.40-2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.08%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>33rd percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

The C++ symbol demangler routine in cplus-dem.c in libiberty, as distributed in GNU Binutils 2.29, allows remote attackers to cause a denial of service (excessive memory allocation and application crash) via a crafted file, as demonstrated by a call from the Binary File Descriptor (BFD) library (aka libbfd).

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 7" src="https://img.shields.io/badge/L-7-fce1a9"/> <!-- unspecified: 0 --><strong>glibc</strong> <code>2.36-9+deb12u7</code> (deb)</summary>

<small><code>pkg:deb/debian/glibc@2.36-9%2Bdeb12u7?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2019-9192?s=debian&n=glibc&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.36-9%2Bdeb12u7"><img alt="low : CVE--2019--9192" src="https://img.shields.io/badge/CVE--2019--9192-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.36-9+deb12u7</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.11%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>44th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

In the GNU C Library (aka glibc or libc6) through 2.29, check_dst_limits_calc_pos_1 in posix/regexec.c has Uncontrolled Recursion, as demonstrated by '(|)(\\1\\1)*' in grep, a different issue than CVE-2018-20796. NOTE: the software maintainer disputes that this is a vulnerability because the behavior occurs only with a crafted pattern

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2019-1010025?s=debian&n=glibc&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.36-9%2Bdeb12u7"><img alt="low : CVE--2019--1010025" src="https://img.shields.io/badge/CVE--2019--1010025-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.36-9+deb12u7</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.35%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>72nd percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

GNU Libc current is affected by: Mitigation bypass. The impact is: Attacker may guess the heap addresses of pthread_created thread. The component is: glibc. NOTE: the vendor's position is "ASLR bypass itself is not a vulnerability.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2019-1010024?s=debian&n=glibc&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.36-9%2Bdeb12u7"><img alt="low : CVE--2019--1010024" src="https://img.shields.io/badge/CVE--2019--1010024-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.36-9+deb12u7</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>2.15%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>89th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

GNU Libc current is affected by: Mitigation bypass. The impact is: Attacker may bypass ASLR using cache of thread stack and heap. The component is: glibc. NOTE: Upstream comments indicate "this is being treated as a non-security bug and no real threat.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2019-1010023?s=debian&n=glibc&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.36-9%2Bdeb12u7"><img alt="low : CVE--2019--1010023" src="https://img.shields.io/badge/CVE--2019--1010023-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.36-9+deb12u7</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>1.20%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>85th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

GNU Libc current is affected by: Re-mapping current loaded library with malicious ELF file. The impact is: In worst case attacker may evaluate privileges. The component is: libld. The attack vector is: Attacker sends 2 ELF files to victim and asks to run ldd on it. ldd execute code. NOTE: Upstream comments indicate "this is being treated as a non-security bug and no real threat.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2019-1010022?s=debian&n=glibc&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.36-9%2Bdeb12u7"><img alt="low : CVE--2019--1010022" src="https://img.shields.io/badge/CVE--2019--1010022-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.36-9+deb12u7</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.41%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>74th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

GNU Libc current is affected by: Mitigation bypass. The impact is: Attacker may bypass stack guard protection. The component is: nptl. The attack vector is: Exploit stack buffer overflow vulnerability and use this bypass vulnerability to bypass stack guard. NOTE: Upstream comments indicate "this is being treated as a non-security bug and no real threat.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2018-20796?s=debian&n=glibc&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.36-9%2Bdeb12u7"><img alt="low : CVE--2018--20796" src="https://img.shields.io/badge/CVE--2018--20796-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.36-9+deb12u7</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.44%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>75th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

In the GNU C Library (aka glibc or libc6) through 2.29, check_dst_limits_calc_pos_1 in posix/regexec.c has Uncontrolled Recursion, as demonstrated by '(\227|)(\\1\\1|t1|\\\2537)+' in grep.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2010-4756?s=debian&n=glibc&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.36-9%2Bdeb12u7"><img alt="low : CVE--2010--4756" src="https://img.shields.io/badge/CVE--2010--4756-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.36-9+deb12u7</code></td></tr>
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
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 4" src="https://img.shields.io/badge/L-4-fce1a9"/> <!-- unspecified: 0 --><strong>patch</strong> <code>2.7.6-7</code> (deb)</summary>

<small><code>pkg:deb/debian/patch@2.7.6-7?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2021-45261?s=debian&n=patch&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.7.6-7"><img alt="low : CVE--2021--45261" src="https://img.shields.io/badge/CVE--2021--45261-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.7.6-7</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.06%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>27th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

An Invalid Pointer vulnerability exists in GNU patch 2.7 via the another_hunk function, which causes a Denial of Service.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2018-6952?s=debian&n=patch&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.7.6-7"><img alt="low : CVE--2018--6952" src="https://img.shields.io/badge/CVE--2018--6952-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.7.6-7</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>3.46%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>92nd percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A double free exists in the another_hunk function in pch.c in GNU patch through 2.7.6.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2018-6951?s=debian&n=patch&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.7.6-7"><img alt="low : CVE--2018--6951" src="https://img.shields.io/badge/CVE--2018--6951-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.7.6-7</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>1.27%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>86th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

An issue was discovered in GNU patch through 2.7.6. There is a segmentation fault, associated with a NULL pointer dereference, leading to a denial of service in the intuit_diff_type function in pch.c, aka a "mangled rename" issue.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2010-4651?s=debian&n=patch&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.7.6-7"><img alt="low : CVE--2010--4651" src="https://img.shields.io/badge/CVE--2010--4651-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.7.6-7</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.55%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>78th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

Directory traversal vulnerability in util.c in GNU patch 2.6.1 and earlier allows user-assisted remote attackers to create or overwrite arbitrary files via a filename that is specified with a .. (dot dot) or full pathname, a related issue to CVE-2010-1679.

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 4" src="https://img.shields.io/badge/L-4-fce1a9"/> <!-- unspecified: 0 --><strong>systemd</strong> <code>252.26-1~deb12u2</code> (deb)</summary>

<small><code>pkg:deb/debian/systemd@252.26-1~deb12u2?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2023-31439?s=debian&n=systemd&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D252.26-1%7Edeb12u2"><img alt="low : CVE--2023--31439" src="https://img.shields.io/badge/CVE--2023--31439-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=252.26-1~deb12u2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.10%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>41st percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

An issue was discovered in systemd 253. An attacker can modify the contents of past events in a sealed log file and then adjust the file such that checking the integrity shows no error, despite modifications. NOTE: the vendor reportedly sent "a reply denying that any of the finding was a security vulnerability."

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2023-31438?s=debian&n=systemd&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D252.26-1%7Edeb12u2"><img alt="low : CVE--2023--31438" src="https://img.shields.io/badge/CVE--2023--31438-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=252.26-1~deb12u2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.10%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>41st percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

An issue was discovered in systemd 253. An attacker can truncate a sealed log file and then resume log sealing such that checking the integrity shows no error, despite modifications. NOTE: the vendor reportedly sent "a reply denying that any of the finding was a security vulnerability."

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2023-31437?s=debian&n=systemd&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D252.26-1%7Edeb12u2"><img alt="low : CVE--2023--31437" src="https://img.shields.io/badge/CVE--2023--31437-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=252.26-1~deb12u2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.09%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>38th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

An issue was discovered in systemd 253. An attacker can modify a sealed log file such that, in some views, not all existing and sealed log messages are displayed. NOTE: the vendor reportedly sent "a reply denying that any of the finding was a security vulnerability."

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2013-4392?s=debian&n=systemd&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D252.26-1%7Edeb12u2"><img alt="low : CVE--2013--4392" src="https://img.shields.io/badge/CVE--2013--4392-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=252.26-1~deb12u2</code></td></tr>
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
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 4" src="https://img.shields.io/badge/L-4-fce1a9"/> <!-- unspecified: 0 --><strong>openldap</strong> <code>2.5.13+dfsg-5</code> (deb)</summary>

<small><code>pkg:deb/debian/openldap@2.5.13%2Bdfsg-5?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2020-15719?s=debian&n=openldap&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.5.13%2Bdfsg-5"><img alt="low : CVE--2020--15719" src="https://img.shields.io/badge/CVE--2020--15719-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.5.13+dfsg-5</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.16%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>54th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

libldap in certain third-party OpenLDAP packages has a certificate-validation flaw when the third-party package is asserting RFC6125 support. It considers CN even when there is a non-matching subjectAltName (SAN). This is fixed in, for example, openldap-2.4.46-10.el8 in Red Hat Enterprise Linux.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2017-17740?s=debian&n=openldap&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.5.13%2Bdfsg-5"><img alt="low : CVE--2017--17740" src="https://img.shields.io/badge/CVE--2017--17740-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.5.13+dfsg-5</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.41%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>74th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

contrib/slapd-modules/nops/nops.c in OpenLDAP through 2.4.45, when both the nops module and the memberof overlay are enabled, attempts to free a buffer that was allocated on the stack, which allows remote attackers to cause a denial of service (slapd crash) via a member MODDN operation.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2017-14159?s=debian&n=openldap&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.5.13%2Bdfsg-5"><img alt="low : CVE--2017--14159" src="https://img.shields.io/badge/CVE--2017--14159-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.5.13+dfsg-5</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.04%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>10th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

slapd in OpenLDAP 2.4.45 and earlier creates a PID file after dropping privileges to a non-root account, which might allow local users to kill arbitrary processes by leveraging access to this non-root account for PID file modification before a root script executes a "kill `cat /pathname`" command, as demonstrated by openldap-initscript.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2015-3276?s=debian&n=openldap&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.5.13%2Bdfsg-5"><img alt="low : CVE--2015--3276" src="https://img.shields.io/badge/CVE--2015--3276-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.5.13+dfsg-5</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.29%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>70th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

The nss_parse_ciphers function in libraries/libldap/tls_m.c in OpenLDAP does not properly parse OpenSSL-style multi-keyword mode cipher strings, which might cause a weaker than intended cipher to be used and allow remote attackers to have unspecified impact via unknown vectors.

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 2" src="https://img.shields.io/badge/L-2-fce1a9"/> <!-- unspecified: 0 --><strong>m4</strong> <code>1.4.19-3</code> (deb)</summary>

<small><code>pkg:deb/debian/m4@1.4.19-3?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2008-1688?s=debian&n=m4&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D1.4.19-3"><img alt="low : CVE--2008--1688" src="https://img.shields.io/badge/CVE--2008--1688-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=1.4.19-3</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>2.87%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>91st percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

Unspecified vulnerability in GNU m4 before 1.4.11 might allow context-dependent attackers to execute arbitrary code, related to improper handling of filenames specified with the -F option.  NOTE: it is not clear when this issue crosses privilege boundaries.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2008-1687?s=debian&n=m4&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D1.4.19-3"><img alt="low : CVE--2008--1687" src="https://img.shields.io/badge/CVE--2008--1687-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=1.4.19-3</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>1.89%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>89th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

The (1) maketemp and (2) mkstemp builtin functions in GNU m4 before 1.4.11 do not quote their output when a file is created, which might allow context-dependent attackers to trigger a macro expansion, leading to unspecified use of an incorrect filename.

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 2" src="https://img.shields.io/badge/L-2-fce1a9"/> <!-- unspecified: 0 --><strong>perl</strong> <code>5.36.0-7+deb12u1</code> (deb)</summary>

<small><code>pkg:deb/debian/perl@5.36.0-7%2Bdeb12u1?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2023-31486?s=debian&n=perl&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D5.36.0-7%2Bdeb12u1"><img alt="low : CVE--2023--31486" src="https://img.shields.io/badge/CVE--2023--31486-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=5.36.0-7+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.29%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>69th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

HTTP::Tiny before 0.083, a Perl core module since 5.13.9 and available standalone on CPAN, has an insecure default TLS configuration where users must opt in to verify certificates.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2011-4116?s=debian&n=perl&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D5.36.0-7%2Bdeb12u1"><img alt="low : CVE--2011--4116" src="https://img.shields.io/badge/CVE--2011--4116-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=5.36.0-7+deb12u1</code></td></tr>
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
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 2" src="https://img.shields.io/badge/L-2-fce1a9"/> <!-- unspecified: 0 --><strong>shadow</strong> <code>1:4.13+dfsg1-1</code> (deb)</summary>

<small><code>pkg:deb/debian/shadow@1:4.13%2Bdfsg1-1?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2019-19882?s=debian&n=shadow&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D1%3A4.13%2Bdfsg1-1"><img alt="low : CVE--2019--19882" src="https://img.shields.io/badge/CVE--2019--19882-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=1:4.13+dfsg1-1</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.04%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>5th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

shadow 4.8, in certain circumstances affecting at least Gentoo, Arch Linux, and Void Linux, allows local users to obtain root access because setuid programs are misconfigured. Specifically, this affects shadow 4.8 when compiled using --with-libpam but without explicitly passing --disable-account-tools-setuid, and without a PAM configuration suitable for use with setuid account management tools. This combination leads to account management tools (groupadd, groupdel, groupmod, useradd, userdel, usermod) that can easily be used by unprivileged local users to escalate privileges to root in multiple ways. This issue became much more relevant in approximately December 2019 when an unrelated bug was fixed (i.e., the chmod calls to suidusbins were fixed in the upstream Makefile which is now included in the release version 4.8).

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2007-5686?s=debian&n=shadow&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D1%3A4.13%2Bdfsg1-1"><img alt="low : CVE--2007--5686" src="https://img.shields.io/badge/CVE--2007--5686-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=1:4.13+dfsg1-1</code></td></tr>
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
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 2" src="https://img.shields.io/badge/L-2-fce1a9"/> <!-- unspecified: 0 --><strong>expat</strong> <code>2.5.0-1</code> (deb)</summary>

<small><code>pkg:deb/debian/expat@2.5.0-1?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2024-28757?s=debian&n=expat&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.5.0-1"><img alt="low : CVE--2024--28757" src="https://img.shields.io/badge/CVE--2024--28757-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.5.0-1</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.04%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>11th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

libexpat through 2.6.1 allows an XML Entity Expansion attack when there is isolated use of external parsers (created via XML_ExternalEntityParserCreate).

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2023-52426?s=debian&n=expat&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.5.0-1"><img alt="low : CVE--2023--52426" src="https://img.shields.io/badge/CVE--2023--52426-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.5.0-1</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.05%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>21st percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

libexpat through 2.5.0 allows recursive XML Entity Expansion if XML_DTD is undefined at compile time.

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 1" src="https://img.shields.io/badge/L-1-fce1a9"/> <!-- unspecified: 0 --><strong>libgcrypt20</strong> <code>1.10.1-3</code> (deb)</summary>

<small><code>pkg:deb/debian/libgcrypt20@1.10.1-3?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2018-6829?s=debian&n=libgcrypt20&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D1.10.1-3"><img alt="low : CVE--2018--6829" src="https://img.shields.io/badge/CVE--2018--6829-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=1.10.1-3</code></td></tr>
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
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 1" src="https://img.shields.io/badge/L-1-fce1a9"/> <!-- unspecified: 0 --><strong>libheif</strong> <code>1.15.1-1</code> (deb)</summary>

<small><code>pkg:deb/debian/libheif@1.15.1-1?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2024-25269?s=debian&n=libheif&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D1.15.1-1"><img alt="low : CVE--2024--25269" src="https://img.shields.io/badge/CVE--2024--25269-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=1.15.1-1</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.04%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>9th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

libheif <= 1.17.6 contains a memory leak in the function JpegEncoder::Encode. This flaw allows an attacker to cause a denial of service attack.

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 1" src="https://img.shields.io/badge/L-1-fce1a9"/> <!-- unspecified: 0 --><strong>openssl</strong> <code>3.0.13-1~deb12u1</code> (deb)</summary>

<small><code>pkg:deb/debian/openssl@3.0.13-1~deb12u1?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2010-0928?s=debian&n=openssl&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D3.0.11-1%7Edeb12u2"><img alt="low : CVE--2010--0928" src="https://img.shields.io/badge/CVE--2010--0928-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=3.0.11-1~deb12u2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.07%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>29th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

OpenSSL 0.9.8i on the Gaisler Research LEON3 SoC on the Xilinx Virtex-II Pro FPGA uses a Fixed Width Exponentiation (FWE) algorithm for certain signature calculations, and does not verify the signature before providing it to a caller, which makes it easier for physically proximate attackers to determine the private key via a modified supply voltage for the microprocessor, related to a "fault-based attack."

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 1" src="https://img.shields.io/badge/L-1-fce1a9"/> <!-- unspecified: 0 --><strong>util-linux</strong> <code>2.38.1-5+deb12u1</code> (deb)</summary>

<small><code>pkg:deb/debian/util-linux@2.38.1-5%2Bdeb12u1?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2022-0563?s=debian&n=util-linux&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.38.1-5%2Bdeb12u1"><img alt="low : CVE--2022--0563" src="https://img.shields.io/badge/CVE--2022--0563-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.38.1-5+deb12u1</code></td></tr>
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
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 1" src="https://img.shields.io/badge/L-1-fce1a9"/> <!-- unspecified: 0 --><strong>coreutils</strong> <code>9.1-1</code> (deb)</summary>

<small><code>pkg:deb/debian/coreutils@9.1-1?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2017-18018?s=debian&n=coreutils&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D9.1-1"><img alt="low : CVE--2017--18018" src="https://img.shields.io/badge/CVE--2017--18018-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=9.1-1</code></td></tr>
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
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 1" src="https://img.shields.io/badge/L-1-fce1a9"/> <!-- unspecified: 0 --><strong>unzip</strong> <code>6.0-28</code> (deb)</summary>

<small><code>pkg:deb/debian/unzip@6.0-28?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2021-4217?s=debian&n=unzip&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D6.0-28"><img alt="low : CVE--2021--4217" src="https://img.shields.io/badge/CVE--2021--4217-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=6.0-28</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.08%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>36th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A flaw was found in unzip. The vulnerability occurs due to improper handling of Unicode strings, which can lead to a null pointer dereference. This flaw allows an attacker to input a specially crafted zip file, leading to a crash or code execution.

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 1" src="https://img.shields.io/badge/L-1-fce1a9"/> <!-- unspecified: 0 --><strong>glib2.0</strong> <code>2.74.6-2+deb12u3</code> (deb)</summary>

<small><code>pkg:deb/debian/glib2.0@2.74.6-2%2Bdeb12u3?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2012-0039?s=debian&n=glib2.0&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.74.6-2%2Bdeb12u3"><img alt="low : CVE--2012--0039" src="https://img.shields.io/badge/CVE--2012--0039-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.74.6-2+deb12u3</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.16%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>52nd percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

GLib 2.31.8 and earlier, when the g_str_hash function is used, computes hash values without restricting the ability to trigger hash collisions predictably, which allows context-dependent attackers to cause a denial of service (CPU consumption) via crafted input to an application that maintains a hash table. NOTE: this issue may be disputed by the vendor; the existence of the g_str_hash function is not a vulnerability in the library, because callers of g_hash_table_new and g_hash_table_new_full can specify an arbitrary hash function that is appropriate for the application.

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 1" src="https://img.shields.io/badge/L-1-fce1a9"/> <!-- unspecified: 0 --><strong>sqlite3</strong> <code>3.40.1-2</code> (deb)</summary>

<small><code>pkg:deb/debian/sqlite3@3.40.1-2?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2021-45346?s=debian&n=sqlite3&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D3.40.1-2"><img alt="low : CVE--2021--45346" src="https://img.shields.io/badge/CVE--2021--45346-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=3.40.1-2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.22%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>61st percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A Memory Leak vulnerability exists in SQLite Project SQLite3 3.35.1 and 3.37.0 via maliciously crafted SQL Queries (made via editing the Database File), it is possible to query a record, and leak subsequent bytes of memory that extend beyond the record, which could let a malicious user obtain sensitive information. NOTE: The developer disputes this as a vulnerability stating that If you give SQLite a corrupted database file and submit a query against the database, it might read parts of the database that you did not intend or expect.

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 1" src="https://img.shields.io/badge/L-1-fce1a9"/> <!-- unspecified: 0 --><strong>pixman</strong> <code>0.42.2-1</code> (deb)</summary>

<small><code>pkg:deb/debian/pixman@0.42.2-1?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2023-37769?s=debian&n=pixman&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D0.42.2-1"><img alt="low : CVE--2023--37769" src="https://img.shields.io/badge/CVE--2023--37769-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=0.42.2-1</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.06%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>28th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

stress-test master commit e4c878 was discovered to contain a FPE vulnerability via the component combine_inner at /pixman-combine-float.c.

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 1" src="https://img.shields.io/badge/L-1-fce1a9"/> <!-- unspecified: 0 --><strong>openexr</strong> <code>3.1.5-5</code> (deb)</summary>

<small><code>pkg:deb/debian/openexr@3.1.5-5?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2017-14988?s=debian&n=openexr&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D3.1.5-5"><img alt="low : CVE--2017--14988" src="https://img.shields.io/badge/CVE--2017--14988-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=3.1.5-5</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.19%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>57th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

Header::readfrom in IlmImf/ImfHeader.cpp in OpenEXR 2.2.0 allows remote attackers to cause a denial of service (excessive memory allocation) via a crafted file that is accessed with the ImfOpenInputFile function in IlmImf/ImfCRgbaFile.cpp. NOTE: The maintainer and multiple third parties believe that this vulnerability isn't valid

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 1" src="https://img.shields.io/badge/L-1-fce1a9"/> <!-- unspecified: 0 --><strong>apt</strong> <code>2.6.1</code> (deb)</summary>

<small><code>pkg:deb/debian/apt@2.6.1?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2011-3374?s=debian&n=apt&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.6.1"><img alt="low : CVE--2011--3374" src="https://img.shields.io/badge/CVE--2011--3374-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.6.1</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.16%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>53rd percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

It was found that apt-key in apt, all versions, do not correctly validate gpg keys with the master keyring, leading to a potential man-in-the-middle attack.

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 1" src="https://img.shields.io/badge/L-1-fce1a9"/> <!-- unspecified: 0 --><strong>krb5</strong> <code>1.20.1-2+deb12u2</code> (deb)</summary>

<small><code>pkg:deb/debian/krb5@1.20.1-2%2Bdeb12u2?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2018-5709?s=debian&n=krb5&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D1.20.1-2%2Bdeb12u1"><img alt="low : CVE--2018--5709" src="https://img.shields.io/badge/CVE--2018--5709-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=1.20.1-2+deb12u1</code></td></tr>
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
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 1" src="https://img.shields.io/badge/L-1-fce1a9"/> <!-- unspecified: 0 --><strong>libpng1.6</strong> <code>1.6.39-2</code> (deb)</summary>

<small><code>pkg:deb/debian/libpng1.6@1.6.39-2?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2021-4214?s=debian&n=libpng1.6&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D1.6.39-2"><img alt="low : CVE--2021--4214" src="https://img.shields.io/badge/CVE--2021--4214-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=1.6.39-2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.05%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>20th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A heap overflow flaw was found in libpngs' pngimage.c program. This flaw allows an attacker with local network access to pass a specially crafted PNG file to the pngimage utility, causing an application to crash, leading to a denial of service.

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 1" src="https://img.shields.io/badge/L-1-fce1a9"/> <!-- unspecified: 0 --><strong>gcc-12</strong> <code>12.2.0-14</code> (deb)</summary>

<small><code>pkg:deb/debian/gcc-12@12.2.0-14?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2022-27943?s=debian&n=gcc-12&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D12.2.0-14"><img alt="low : CVE--2022--27943" src="https://img.shields.io/badge/CVE--2022--27943-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=12.2.0-14</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.07%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>32nd percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

libiberty/rust-demangle.c in GNU GCC 11.2 allows stack consumption in demangle_const, as demonstrated by nm-new.

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 1" src="https://img.shields.io/badge/L-1-fce1a9"/> <!-- unspecified: 0 --><strong>jansson</strong> <code>2.14-2</code> (deb)</summary>

<small><code>pkg:deb/debian/jansson@2.14-2?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2020-36325?s=debian&n=jansson&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.14-2"><img alt="low : CVE--2020--36325" src="https://img.shields.io/badge/CVE--2020--36325-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.14-2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.16%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>53rd percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

An issue was discovered in Jansson through 2.13.1. Due to a parsing error in json_loads, there's an out-of-bounds read-access bug. NOTE: the vendor reports that this only occurs when a programmer fails to follow the API specification

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 1" src="https://img.shields.io/badge/L-1-fce1a9"/> <!-- unspecified: 0 --><strong>tar</strong> <code>1.34+dfsg-1.2+deb12u1</code> (deb)</summary>

<small><code>pkg:deb/debian/tar@1.34%2Bdfsg-1.2%2Bdeb12u1?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2005-2541?s=debian&n=tar&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D1.34%2Bdfsg-1.2%2Bdeb12u1"><img alt="low : CVE--2005--2541" src="https://img.shields.io/badge/CVE--2005--2541-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=1.34+dfsg-1.2+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.69%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>80th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

Tar 1.15.1 does not properly warn the user when extracting setuid or setgid files, which may allow local users or remote attackers to gain privileges.

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 1" src="https://img.shields.io/badge/L-1-fce1a9"/> <!-- unspecified: 0 --><strong>python3.11</strong> <code>3.11.2-6+deb12u2</code> (deb)</summary>

<small><code>pkg:deb/debian/python3.11@3.11.2-6%2Bdeb12u2?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2024-3219?s=debian&n=python3.11&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D3.11.2-6%2Bdeb12u2"><img alt="low : CVE--2024--3219" src="https://img.shields.io/badge/CVE--2024--3219-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=3.11.2-6+deb12u2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

There is a MEDIUM severity vulnerability affecting CPython.  The  “socket” module provides a pure-Python fallback to the  socket.socketpair() function for platforms that don’t support AF_UNIX,  such as Windows. This pure-Python implementation uses AF_INET or  AF_INET6 to create a local connected pair of sockets. The connection  between the two sockets was not verified before passing the two sockets  back to the user, which leaves the server socket vulnerable to a  connection race from a malicious local peer.  Platforms that support AF_UNIX such as Linux and macOS are not affected by this vulnerability. Versions prior to CPython 3.5 are not affected due to the vulnerable API not being included.

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 1" src="https://img.shields.io/badge/L-1-fce1a9"/> <!-- unspecified: 0 --><strong>gnutls28</strong> <code>3.7.9-2+deb12u3</code> (deb)</summary>

<small><code>pkg:deb/debian/gnutls28@3.7.9-2%2Bdeb12u3?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2011-3389?s=debian&n=gnutls28&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D3.7.9-2%2Bdeb12u3"><img alt="low : CVE--2011--3389" src="https://img.shields.io/badge/CVE--2011--3389-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=3.7.9-2+deb12u3</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.85%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>82nd percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

The SSL protocol, as used in certain configurations in Microsoft Windows and Microsoft Internet Explorer, Mozilla Firefox, Google Chrome, Opera, and other products, encrypts data by using CBC mode with chained initialization vectors, which allows man-in-the-middle attackers to obtain plaintext HTTP headers via a blockwise chosen-boundary attack (BCBA) on an HTTPS session, in conjunction with JavaScript code that uses (1) the HTML5 WebSocket API, (2) the Java URLConnection API, or (3) the Silverlight WebClient API, aka a "BEAST" attack.

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 1" src="https://img.shields.io/badge/L-1-fce1a9"/> <!-- unspecified: 0 --><strong>gnupg2</strong> <code>2.2.40-1.1</code> (deb)</summary>

<small><code>pkg:deb/debian/gnupg2@2.2.40-1.1?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2022-3219?s=debian&n=gnupg2&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.2.40-1.1"><img alt="low : CVE--2022--3219" src="https://img.shields.io/badge/CVE--2022--3219-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.2.40-1.1</code></td></tr>
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
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 1" src="https://img.shields.io/badge/L-1-fce1a9"/> <!-- unspecified: 0 --><strong>libxml2</strong> <code>2.9.14+dfsg-1.3~deb12u1</code> (deb)</summary>

<small><code>pkg:deb/debian/libxml2@2.9.14%2Bdfsg-1.3~deb12u1?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2024-34459?s=debian&n=libxml2&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.9.14%2Bdfsg-1.3%7Edeb12u1"><img alt="low : CVE--2024--34459" src="https://img.shields.io/badge/CVE--2024--34459-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.9.14+dfsg-1.3~deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.04%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>11th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

An issue was discovered in xmllint (from libxml2) before 2.11.8 and 2.12.x before 2.12.7. Formatting error messages with xmllint --htmlout can result in a buffer over-read in xmlHTMLPrintFileContext in xmllint.c.

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 1" src="https://img.shields.io/badge/L-1-fce1a9"/> <!-- unspecified: 0 --><strong>elfutils</strong> <code>0.188-2.1</code> (deb)</summary>

<small><code>pkg:deb/debian/elfutils@0.188-2.1?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2024-25260?s=debian&n=elfutils&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D0.188-2.1"><img alt="low : CVE--2024--25260" src="https://img.shields.io/badge/CVE--2024--25260-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=0.188-2.1</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.04%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>16th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

elfutils v0.189 was discovered to contain a NULL pointer dereference via the handle_verdef() function at readelf.c.

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 1" src="https://img.shields.io/badge/L-1-fce1a9"/> <!-- unspecified: 0 --><strong>tcl8.6</strong> <code>8.6.13+dfsg-2</code> (deb)</summary>

<small><code>pkg:deb/debian/tcl8.6@8.6.13%2Bdfsg-2?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2021-35331?s=debian&n=tcl8.6&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D8.6.13%2Bdfsg-2"><img alt="low : CVE--2021--35331" src="https://img.shields.io/badge/CVE--2021--35331-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=8.6.13+dfsg-2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.41%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>74th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

In Tcl 8.6.11, a format string vulnerability in nmakehlp.c might allow code execution via a crafted file. NOTE: multiple third parties dispute the significance of this finding

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 1" src="https://img.shields.io/badge/L-1-fce1a9"/> <!-- unspecified: 0 --><strong>curl</strong> <code>7.88.1-10+deb12u6</code> (deb)</summary>

<small><code>pkg:deb/debian/curl@7.88.1-10%2Bdeb12u6?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2024-2379?s=debian&n=curl&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D7.88.1-10%2Bdeb12u6"><img alt="low : CVE--2024--2379" src="https://img.shields.io/badge/CVE--2024--2379-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=7.88.1-10+deb12u6</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.04%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>16th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

libcurl skips the certificate verification for a QUIC connection under certain conditions, when built to use wolfSSL. If told to use an unknown/bad cipher or curve, the error path accidentally skips the verification and returns OK, thus ignoring any certificate problems.

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 1" src="https://img.shields.io/badge/L-1-fce1a9"/> <!-- unspecified: 0 --><strong>libxslt</strong> <code>1.1.35-1</code> (deb)</summary>

<small><code>pkg:deb/debian/libxslt@1.1.35-1?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2015-9019?s=debian&n=libxslt&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D1.1.35-1"><img alt="low : CVE--2015--9019" src="https://img.shields.io/badge/CVE--2015--9019-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=1.1.35-1</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.09%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>39th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

In libxslt 1.1.29 and earlier, the EXSLT math.random function was not initialized with a random seed during startup, which could cause usage of this function to produce predictable outputs.

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 1" src="https://img.shields.io/badge/L-1-fce1a9"/> <!-- unspecified: 0 --><strong>jbigkit</strong> <code>2.1-6.1</code> (deb)</summary>

<small><code>pkg:deb/debian/jbigkit@2.1-6.1?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2017-9937?s=debian&n=jbigkit&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.1-6.1"><img alt="low : CVE--2017--9937" src="https://img.shields.io/badge/CVE--2017--9937-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.1-6.1</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.14%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>51st percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

In LibTIFF 4.0.8, there is a memory malloc failure in tif_jbig.c. A crafted TIFF document can lead to an abort resulting in a remote denial of service attack.

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 0" src="https://img.shields.io/badge/L-0-lightgrey"/> <img alt="unspecified: 2" src="https://img.shields.io/badge/U-2-lightgrey"/><strong>libyaml</strong> <code>0.2.5-1</code> (deb)</summary>

<small><code>pkg:deb/debian/libyaml@0.2.5-1?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2024-35329?s=debian&n=libyaml&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D0.2.5-1"><img alt="unspecified : CVE--2024--35329" src="https://img.shields.io/badge/CVE--2024--35329-lightgrey?label=unspecified%20&labelColor=lightgrey"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=0.2.5-1</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.04%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>9th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

libyaml 0.2.5 is vulnerable to a heap-based Buffer Overflow in yaml_document_add_sequence in api.c.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2024-3205?s=debian&n=libyaml&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D0.2.5-1"><img alt="unspecified : CVE--2024--3205" src="https://img.shields.io/badge/CVE--2024--3205-lightgrey?label=unspecified%20&labelColor=lightgrey"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=0.2.5-1</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.04%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>9th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A vulnerability was found in yaml libyaml up to 0.2.5 and classified as critical. Affected by this issue is the function yaml_emitter_emit_flow_sequence_item of the file /src/libyaml/src/emitter.c. The manipulation leads to heap-based buffer overflow. The attack may be launched remotely. The exploit has been disclosed to the public and may be used. The identifier of this vulnerability is VDB-259052. NOTE: The vendor was contacted early about this disclosure but did not respond in any way.

</blockquote>
</details>
</details></td></tr>
</table>

