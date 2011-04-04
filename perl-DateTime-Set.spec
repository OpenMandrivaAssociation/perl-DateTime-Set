%define upstream_name    DateTime-Set
%define upstream_version 0.30

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Extends Set::Infinite with recurrence functions
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/DateTime/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(DateTime)
BuildRequires: perl(Set::Infinite)
BuildRequires: perl(Test::More)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
DateTime::Set is a module for datetime sets. It can be used to handle two
different types of sets.

The first is a fixed set of predefined datetime objects. For example, if we
wanted to create a set of datetimes containing the birthdays of people in
our family for the current year.

The second type of set that it can handle is one based on a recurrence,
such as "every Wednesday", or "noon on the 15th day of every month". This
type of set can have fixed starting and ending datetimes, but neither is
required. So our "every Wednesday set" could be "every Wednesday from the
beginning of time until the end of time", or "every Wednesday after
2003-03-05 until the end of time", or "every Wednesday between 2003-03-05
and 2004-01-07".

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes LICENSE META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*


