Summary:	Standard input and output buffering program
Summary(pl):	Program buforuj±cy standardowe wej¶cie i wyj¶cie
Name:		buffer
Version:	1.19
Release:	2
License:	GPL
Group:		Applications/Archiving
Source0:	http://www.netsw.org/system/tools/fileutils/filter/%{name}-%{version}.shar.gz
Patch0:		%{name}-1.17_suse.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Standard input and output buffering program.

%description -l pl
Program buforuj±cy standardowe wej¶cie i wyj¶cie.

%prep
%setup -q -T -c -n buffer-%{version}
gzip -dc %{SOURCE0} > %{name}-%{version}.shar
chmod 755 %{name}-%{version}.shar
./%{name}-%{version}.shar
%patch0 -p0

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

%{__make} install CFLAGS="%{rpmcflags}" \
	INSTBIN=$RPM_BUILD_ROOT%{_bindir} INSTMAN=$RPM_BUILD_ROOT%{_mandir}/man1

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README*
%attr(755,root,root) %{_bindir}/buffer
%{_mandir}/man1/buffer*
