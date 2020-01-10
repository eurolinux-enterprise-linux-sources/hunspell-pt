Name: hunspell-pt
Summary: Portuguese hunspell dictionaries
%define upstreamid 20130125
Version: 0.%{upstreamid}
Release: 1%{?dist}
Source0: http://natura.di.uminho.pt/download/sources/Dictionaries/hunspell/hunspell-pt_PT-20130125.tar.gz
Source1: http://extensions.libreoffice.org/extension-center/vero-verificador-ortografico-e-hifenizador-em-portugues-do-brasil/pscreleasefolder.2012-01-04.1563120832/2.1/vero_pt_br_v210aoc.oxt
Group: Applications/Text
URL: http://www.broffice.org/verortografico/baixar
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
# pt_BR dicts are under LGPLv3 or MPL, pt_PT under GPLv2 or LGPLv2 or MPLv1.1
License: ((LGPLv3 or MPL) and LGPLv2) and (GPLv2 or LGPLv2 or MPLv1.1)
BuildArch: noarch

Requires: hunspell

%description
Portuguese hunspell dictionaries.

%prep
%setup -q -n hunspell-pt_PT-20130125
unzip -q -o %{SOURCE1}
for i in README_pt_BR.TXT README_pt_PT.txt; do
  if ! iconv -f utf-8 -t utf-8 -o /dev/null $i > /dev/null 2>&1; then
    iconv -f ISO-8859-1 -t UTF-8 $i > $i.new
    touch -r $i $i.new
    mv -f $i.new $i
  fi
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p pt*.dic pt*.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

pushd $RPM_BUILD_ROOT/%{_datadir}/myspell/
pt_PT_aliases="pt_AO"
for lang in $pt_PT_aliases; do
        ln -s pt_PT.aff $lang.aff
        ln -s pt_PT.dic $lang.dic
done
popd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README_pt_BR.TXT README_pt_PT.txt COPYING
%{_datadir}/myspell/*

%changelog
* Thu Jan 31 2013 Caolán McNamara <caolanm@redhat.com> - 0.20130125-1
- latest pt_PT version

* Wed Sep 12 2012 Caolán McNamara <caolanm@redhat.com> - 0.20120911-1
- latest pt_PT version

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20120611-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 13 2012 Caolán McNamara <caolanm@redhat.com> - 0.20120611-1
- latest pt_PT version

* Tue May 08 2012 Caolán McNamara <caolanm@redhat.com> - 0.20120312-2
- alias pt_AO to pt_PT instead

* Tue Apr 10 2012 Caolán McNamara <caolanm@redhat.com> - 0.20120312-1
- latest pt_PT and pt_BR versions
- alias pt_AO to pt_BR (post-1990 orthographic accord)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20111102-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov 16 2011 Caolán McNamara <caolanm@redhat.com> - 0.20111102-1
- latest pt_PT version

* Mon Oct 17 2011 Caolán McNamara <caolanm@redhat.com> - 0.20110928-1
- latest pt_PT version

* Fri Aug 26 2011 Caolán McNamara <caolanm@redhat.com> - 0.20110823-1
- latest pt_PT version

* Thu Jun 09 2011 Caolán McNamara <caolanm@redhat.com> - 0.20110608-1
- latest pt_PT and pt_BR versions

* Sat Apr 02 2011 Caolán McNamara <caolanm@redhat.com> - 0.20110331-1
- latest pt_PT version

* Fri Mar 18 2011 Caolán McNamara <caolanm@redhat.com> - 0.20110318-1
- latest pt_PT version

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20101214-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 21 2010 Caolán McNamara <caolanm@redhat.com> - 0.20101214-1
- latest pt_PT version

* Wed Nov 10 2010 Caolán McNamara <caolanm@redhat.com> - 0.20101104-1
- latest pt_PT version

* Wed Nov 03 2010 Caolán McNamara <caolanm@redhat.com> - 0.20101031-1
- latest pt_PT version

* Sun Oct 31 2010 Caolán McNamara <caolanm@redhat.com> - 0.20101030-1
- latest pt_PT version

* Thu Oct 28 2010 Caolán McNamara <caolanm@redhat.com> - 0.20101027-1
- latest pt_PT version

* Wed Jun 09 2010 Caolán McNamara <caolanm@redhat.com> - 0.20100907-1
- latest pt_BR version

* Wed Jun 09 2010 Caolán McNamara <caolanm@redhat.com> - 0.20100109-2
- Resolves: rhbz#602193 clarify licences

* Sun Jan 10 2010 Caolán McNamara <caolanm@redhat.com> - 0.20100109-1
- latest pt_BR version

* Thu Oct 15 2009 Caolán McNamara <caolanm@redhat.com> - 0.20091013-1
- latest pt_PT version

* Tue Oct 06 2009 Caolán McNamara <caolanm@redhat.com> - 0.20091004-1
- latest pt_BR version

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20090702-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jul 11 2009 Caolán McNamara <caolanm@redhat.com> - 0.20090702-2
- tidy spec

* Fri Jul 03 2009 Caolán McNamara <caolanm@redhat.com> - 0.20090702-1
- latest pt_BR version

* Thu Apr 30 2009 Caolán McNamara <caolanm@redhat.com> - 0.20090330-1
- latest pt_BR version

* Tue Mar 10 2009 Caolán McNamara <caolanm@redhat.com> - 0.20090309-1
- latest pt_PT version

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20081113-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Nov 23 2008 Caolán McNamara <caolanm@redhat.com> - 0.20081113-1
- latest pt_PT version

* Tue Jul 08 2008 Caolán McNamara <caolanm@redhat.com> - 0.20080707-1
- latest pt_BR version

* Mon Jul 07 2008 Caolán McNamara <caolanm@redhat.com> - 0.20080705-1
- latest pt_PT version

* Tue Jun 10 2008 Caolán McNamara <caolanm@redhat.com> - 0.20080610-1
- latest version

* Fri Mar 21 2008 Caolán McNamara <caolanm@redhat.com> - 0.20080320-1
- latest version

* Thu Feb 21 2008 Caolán McNamara <caolanm@redhat.com> - 0.20080221-1
- latest version

* Fri Feb 15 2008 Caolán McNamara <caolanm@redhat.com> - 0.20080210-1
- latest version

* Fri Dec 14 2007 Caolán McNamara <caolanm@redhat.com> - 0.20071212-1
- latest version

* Sat Nov 11 2007 Caolán McNamara <caolanm@redhat.com> - 0.20071106-1
- latest version

* Mon Nov 05 2007 Caolán McNamara <caolanm@redhat.com> - 0.20071101-1
- latest version

* Fri Oct 05 2007 Caolán McNamara <caolanm@redhat.com> - 0.20071003-1
- next version

* Tue Oct 02 2007 Caolán McNamara <caolanm@redhat.com> - 0.20071001-1
- next version

* Tue Aug 28 2007 Caolán McNamara <caolanm@redhat.com> - 0.20070823-2
- source file audit shows that pt_BR-2007-04-11.zip silently changed
  content, updating to match

* Thu Aug 23 2007 Caolán McNamara <caolanm@redhat.com> - 0.20070823-1
- latest version

* Fri Aug 03 2007 Caolán McNamara <caolanm@redhat.com> - 0.20070709-2
- clarify licences

* Wed Jul 18 2007 Caolán McNamara <caolanm@redhat.com> - 0.20070709-1
- latest pt_PT version

* Sun May 06 2007 Caolán McNamara <caolanm@redhat.com> - 0.20070411-1
- latest versions

* Wed Feb 14 2007 Caolán McNamara <caolanm@redhat.com> - 0.20061026-2
- disambiguate readmes

* Thu Dec 07 2006 Caolán McNamara <caolanm@redhat.com> - 0.20061026-1
- initial version
