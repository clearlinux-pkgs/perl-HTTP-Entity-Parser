#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-HTTP-Entity-Parser
Version  : 0.21
Release  : 2
URL      : https://cpan.metacpan.org/authors/id/K/KA/KAZEBURO/HTTP-Entity-Parser-0.21.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/K/KA/KAZEBURO/HTTP-Entity-Parser-0.21.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libh/libhttp-entity-parser-perl/libhttp-entity-parser-perl_0.21-1.debian.tar.xz
Summary  : 'PSGI compliant HTTP Entity Parser'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-HTTP-Entity-Parser-license = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(ExtUtils::Config)
BuildRequires : perl(ExtUtils::Helpers)
BuildRequires : perl(ExtUtils::InstallPaths)
BuildRequires : perl(Module::Build::Tiny)

%description
# NAME
HTTP::Entity::Parser - PSGI compliant HTTP Entity Parser
# SYNOPSIS
use HTTP::Entity::Parser;

%package dev
Summary: dev components for the perl-HTTP-Entity-Parser package.
Group: Development
Provides: perl-HTTP-Entity-Parser-devel = %{version}-%{release}

%description dev
dev components for the perl-HTTP-Entity-Parser package.


%package license
Summary: license components for the perl-HTTP-Entity-Parser package.
Group: Default

%description license
license components for the perl-HTTP-Entity-Parser package.


%prep
%setup -q -n HTTP-Entity-Parser-0.21
cd ..
%setup -q -T -D -n HTTP-Entity-Parser-0.21 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/HTTP-Entity-Parser-0.21/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-HTTP-Entity-Parser
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-HTTP-Entity-Parser/LICENSE
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.0/HTTP/Entity/Parser.pm
/usr/lib/perl5/vendor_perl/5.28.0/HTTP/Entity/Parser/JSON.pm
/usr/lib/perl5/vendor_perl/5.28.0/HTTP/Entity/Parser/MultiPart.pm
/usr/lib/perl5/vendor_perl/5.28.0/HTTP/Entity/Parser/OctetStream.pm
/usr/lib/perl5/vendor_perl/5.28.0/HTTP/Entity/Parser/UrlEncoded.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/HTTP::Entity::Parser.3
/usr/share/man/man3/HTTP::Entity::Parser::JSON.3
/usr/share/man/man3/HTTP::Entity::Parser::MultiPart.3
/usr/share/man/man3/HTTP::Entity::Parser::OctetStream.3
/usr/share/man/man3/HTTP::Entity::Parser::UrlEncoded.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-HTTP-Entity-Parser/LICENSE
