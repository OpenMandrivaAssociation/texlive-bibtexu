# revision 26693
# category TLCore
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-bibtexu
Version:	20120807
Release:	1
Summary:	TeXLive bibtexu package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bibtexu.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bibtexu.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-bibtexu.bin

%description
TeXLive bibtexu package.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdir}/doc/bibtexu/00readme.txt
%doc %{_texmfdir}/doc/bibtexu/HISTORY
%doc %{_texmfdir}/doc/bibtexu/csfile.txt
%doc %{_texmfdir}/doc/bibtexu/file_id.diz

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf %{buildroot}%{_datadir}


%changelog
* Tue Aug 07 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120807-1
+ Revision: 812075
- Update to latest release.

* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 20111103-2
+ Revision: 749695
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20111103-1
+ Revision: 720153
- texlive-bibtexu
- texlive-bibtexu
- texlive-bibtexu
- texlive-bibtexu

