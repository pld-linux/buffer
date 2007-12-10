Summary:	Standard input and output buffering program
Summary(pl.UTF-8):	Program buforujący standardowe wejście i wyjście
Name:		buffer
Version:	1.19
Release:	3
License:	GPL
Group:		Applications/Archiving
Source0:	http://www.netsw.org/system/tools/fileutils/filter/%{name}-%{version}.shar.gz
# Source0-md5:	b53ffff6380118f77b4f6cb4784a70db
Patch0:		%{name}-1.17_suse.patch
Patch1:		%{name}-debian-1.19-7.patch
Patch2:		%{name}-largefile.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Standard input and output buffering program.

%description -l pl.UTF-8
Program buforujący standardowe wejście i wyjście.

%prep
%setup -q -T -c -n buffer-%{version}
gzip -dc %{SOURCE0} > %{name}-%{version}.shar
chmod 755 %{name}-%{version}.shar
./%{name}-%{version}.shar
%patch0 -p0
%patch1 -p1
%patch2 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install buffer $RPM_BUILD_ROOT%{_bindir}
install buffer.man $RPM_BUILD_ROOT%{_mandir}/man1/buffer.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/buffer
%{_mandir}/man1/buffer*
