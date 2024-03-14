#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v4
# autospec commit: 3d985eb
#
# Source0 file verified with key 0xD7574483BB57B18D (jr@jriddell.org)
#
Name     : kdiagram
Version  : 3.0.1
Release  : 7
URL      : https://download.kde.org/stable/kdiagram/3.0.1/kdiagram-3.0.1.tar.xz
Source0  : https://download.kde.org/stable/kdiagram/3.0.1/kdiagram-3.0.1.tar.xz
Source1  : https://download.kde.org/stable/kdiagram/3.0.1/kdiagram-3.0.1.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.0
Requires: kdiagram-data = %{version}-%{release}
Requires: kdiagram-lib = %{version}-%{release}
Requires: kdiagram-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Running the examples
The examples are only compiled automatically if you pass the -unittests option
to configure. This is because some examples require the "testtools" internal
library that is not installed when configured without -unittests.

%package data
Summary: data components for the kdiagram package.
Group: Data

%description data
data components for the kdiagram package.


%package dev
Summary: dev components for the kdiagram package.
Group: Development
Requires: kdiagram-lib = %{version}-%{release}
Requires: kdiagram-data = %{version}-%{release}
Provides: kdiagram-devel = %{version}-%{release}
Requires: kdiagram = %{version}-%{release}

%description dev
dev components for the kdiagram package.


%package lib
Summary: lib components for the kdiagram package.
Group: Libraries
Requires: kdiagram-data = %{version}-%{release}
Requires: kdiagram-license = %{version}-%{release}

%description lib
lib components for the kdiagram package.


%package license
Summary: license components for the kdiagram package.
Group: Default

%description license
license components for the kdiagram package.


%prep
%setup -q -n kdiagram-3.0.1
cd %{_builddir}/kdiagram-3.0.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1710437417
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1710437417
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kdiagram
cp %{_builddir}/kdiagram-%{version}/LICENSE.GPL.txt %{buildroot}/usr/share/package-licenses/kdiagram/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/kdiagram-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kdiagram/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
cp %{_builddir}/kdiagram-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kdiagram/a4c60b3fefda228cd7439d3565df043192fef137 || :
export GOAMD64=v2
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/qt6/mkspecs/modules/qt_KChart6.pri
/usr/lib64/qt6/mkspecs/modules/qt_KGantt6.pri

%files data
%defattr(-,root,root,-)
/usr/share/locale/ar/LC_MESSAGES/kchart6_qt.qm
/usr/share/locale/ar/LC_MESSAGES/kgantt6_qt.qm
/usr/share/locale/bg/LC_MESSAGES/kchart6_qt.qm
/usr/share/locale/bg/LC_MESSAGES/kgantt6_qt.qm
/usr/share/locale/bs/LC_MESSAGES/kchart6_qt.qm
/usr/share/locale/bs/LC_MESSAGES/kgantt6_qt.qm
/usr/share/locale/ca/LC_MESSAGES/kchart6_qt.qm
/usr/share/locale/ca/LC_MESSAGES/kgantt6_qt.qm
/usr/share/locale/ca@valencia/LC_MESSAGES/kchart6_qt.qm
/usr/share/locale/ca@valencia/LC_MESSAGES/kgantt6_qt.qm
/usr/share/locale/cs/LC_MESSAGES/kchart6_qt.qm
/usr/share/locale/cs/LC_MESSAGES/kgantt6_qt.qm
/usr/share/locale/da/LC_MESSAGES/kgantt6_qt.qm
/usr/share/locale/de/LC_MESSAGES/kchart6_qt.qm
/usr/share/locale/de/LC_MESSAGES/kgantt6_qt.qm
/usr/share/locale/el/LC_MESSAGES/kchart6_qt.qm
/usr/share/locale/el/LC_MESSAGES/kgantt6_qt.qm
/usr/share/locale/en_GB/LC_MESSAGES/kchart6_qt.qm
/usr/share/locale/en_GB/LC_MESSAGES/kgantt6_qt.qm
/usr/share/locale/eo/LC_MESSAGES/kchart6_qt.qm
/usr/share/locale/eo/LC_MESSAGES/kgantt6_qt.qm
/usr/share/locale/es/LC_MESSAGES/kchart6_qt.qm
/usr/share/locale/es/LC_MESSAGES/kgantt6_qt.qm
/usr/share/locale/et/LC_MESSAGES/kchart6_qt.qm
/usr/share/locale/et/LC_MESSAGES/kgantt6_qt.qm
/usr/share/locale/eu/LC_MESSAGES/kchart6_qt.qm
/usr/share/locale/eu/LC_MESSAGES/kgantt6_qt.qm
/usr/share/locale/fi/LC_MESSAGES/kchart6_qt.qm
/usr/share/locale/fi/LC_MESSAGES/kgantt6_qt.qm
/usr/share/locale/fr/LC_MESSAGES/kchart6_qt.qm
/usr/share/locale/fr/LC_MESSAGES/kgantt6_qt.qm
/usr/share/locale/gl/LC_MESSAGES/kchart6_qt.qm
/usr/share/locale/gl/LC_MESSAGES/kgantt6_qt.qm
/usr/share/locale/ia/LC_MESSAGES/kchart6_qt.qm
/usr/share/locale/ia/LC_MESSAGES/kgantt6_qt.qm
/usr/share/locale/it/LC_MESSAGES/kchart6_qt.qm
/usr/share/locale/it/LC_MESSAGES/kgantt6_qt.qm
/usr/share/locale/ja/LC_MESSAGES/kchart6_qt.qm
/usr/share/locale/ja/LC_MESSAGES/kgantt6_qt.qm
/usr/share/locale/ka/LC_MESSAGES/kchart6_qt.qm
/usr/share/locale/ka/LC_MESSAGES/kgantt6_qt.qm
/usr/share/locale/ko/LC_MESSAGES/kchart6_qt.qm
/usr/share/locale/ko/LC_MESSAGES/kgantt6_qt.qm
/usr/share/locale/lt/LC_MESSAGES/kchart6_qt.qm
/usr/share/locale/lt/LC_MESSAGES/kgantt6_qt.qm
/usr/share/locale/nl/LC_MESSAGES/kchart6_qt.qm
/usr/share/locale/nl/LC_MESSAGES/kgantt6_qt.qm
/usr/share/locale/nn/LC_MESSAGES/kchart6_qt.qm
/usr/share/locale/nn/LC_MESSAGES/kgantt6_qt.qm
/usr/share/locale/pl/LC_MESSAGES/kchart6_qt.qm
/usr/share/locale/pl/LC_MESSAGES/kgantt6_qt.qm
/usr/share/locale/pt/LC_MESSAGES/kchart6_qt.qm
/usr/share/locale/pt/LC_MESSAGES/kgantt6_qt.qm
/usr/share/locale/pt_BR/LC_MESSAGES/kchart6_qt.qm
/usr/share/locale/pt_BR/LC_MESSAGES/kgantt6_qt.qm
/usr/share/locale/ro/LC_MESSAGES/kchart6_qt.qm
/usr/share/locale/ru/LC_MESSAGES/kchart6_qt.qm
/usr/share/locale/ru/LC_MESSAGES/kgantt6_qt.qm
/usr/share/locale/sk/LC_MESSAGES/kchart6_qt.qm
/usr/share/locale/sk/LC_MESSAGES/kgantt6_qt.qm
/usr/share/locale/sl/LC_MESSAGES/kchart6_qt.qm
/usr/share/locale/sl/LC_MESSAGES/kgantt6_qt.qm
/usr/share/locale/sv/LC_MESSAGES/kchart6_qt.qm
/usr/share/locale/sv/LC_MESSAGES/kgantt6_qt.qm
/usr/share/locale/tr/LC_MESSAGES/kchart6_qt.qm
/usr/share/locale/tr/LC_MESSAGES/kgantt6_qt.qm
/usr/share/locale/uk/LC_MESSAGES/kchart6_qt.qm
/usr/share/locale/uk/LC_MESSAGES/kgantt6_qt.qm
/usr/share/locale/zh_CN/LC_MESSAGES/kchart6_qt.qm
/usr/share/locale/zh_CN/LC_MESSAGES/kgantt6_qt.qm
/usr/share/locale/zh_TW/LC_MESSAGES/kchart6_qt.qm
/usr/share/locale/zh_TW/LC_MESSAGES/kgantt6_qt.qm

%files dev
%defattr(-,root,root,-)
/usr/include/KChart6/KChart
/usr/include/KChart6/KChartAbstractArea
/usr/include/KChart6/KChartAbstractArea.h
/usr/include/KChart6/KChartAbstractAreaBase
/usr/include/KChart6/KChartAbstractAreaBase.h
/usr/include/KChart6/KChartAbstractAreaWidget
/usr/include/KChart6/KChartAbstractAreaWidget.h
/usr/include/KChart6/KChartAbstractAxis
/usr/include/KChart6/KChartAbstractAxis.h
/usr/include/KChart6/KChartAbstractCartesianDiagram
/usr/include/KChart6/KChartAbstractCartesianDiagram.h
/usr/include/KChart6/KChartAbstractCoordinatePlane
/usr/include/KChart6/KChartAbstractCoordinatePlane.h
/usr/include/KChart6/KChartAbstractDiagram
/usr/include/KChart6/KChartAbstractDiagram.h
/usr/include/KChart6/KChartAbstractPieDiagram
/usr/include/KChart6/KChartAbstractPieDiagram.h
/usr/include/KChart6/KChartAbstractPolarDiagram
/usr/include/KChart6/KChartAbstractPolarDiagram.h
/usr/include/KChart6/KChartAbstractProxyModel
/usr/include/KChart6/KChartAbstractProxyModel.h
/usr/include/KChart6/KChartAbstractTernaryDiagram
/usr/include/KChart6/KChartAbstractTernaryDiagram.h
/usr/include/KChart6/KChartAbstractThreeDAttributes
/usr/include/KChart6/KChartAbstractThreeDAttributes.h
/usr/include/KChart6/KChartAttributesModel
/usr/include/KChart6/KChartAttributesModel.h
/usr/include/KChart6/KChartBackgroundAttributes
/usr/include/KChart6/KChartBackgroundAttributes.h
/usr/include/KChart6/KChartBarAttributes
/usr/include/KChart6/KChartBarAttributes.h
/usr/include/KChart6/KChartBarDiagram
/usr/include/KChart6/KChartBarDiagram.h
/usr/include/KChart6/KChartCartesianAxis
/usr/include/KChart6/KChartCartesianAxis.h
/usr/include/KChart6/KChartCartesianCoordinatePlane
/usr/include/KChart6/KChartCartesianCoordinatePlane.h
/usr/include/KChart6/KChartChart
/usr/include/KChart6/KChartChart.h
/usr/include/KChart6/KChartDataValueAttributes
/usr/include/KChart6/KChartDataValueAttributes.h
/usr/include/KChart6/KChartDatasetProxyModel
/usr/include/KChart6/KChartDatasetProxyModel.h
/usr/include/KChart6/KChartDatasetSelector
/usr/include/KChart6/KChartDatasetSelector.h
/usr/include/KChart6/KChartDiagramObserver
/usr/include/KChart6/KChartDiagramObserver.h
/usr/include/KChart6/KChartEnums
/usr/include/KChart6/KChartEnums.h
/usr/include/KChart6/KChartFrameAttributes
/usr/include/KChart6/KChartFrameAttributes.h
/usr/include/KChart6/KChartGlobal
/usr/include/KChart6/KChartGlobal.h
/usr/include/KChart6/KChartGridAttributes
/usr/include/KChart6/KChartGridAttributes.h
/usr/include/KChart6/KChartHeaderFooter
/usr/include/KChart6/KChartHeaderFooter.h
/usr/include/KChart6/KChartLayoutItems
/usr/include/KChart6/KChartLayoutItems.h
/usr/include/KChart6/KChartLegend
/usr/include/KChart6/KChartLegend.h
/usr/include/KChart6/KChartLeveyJenningsAxis
/usr/include/KChart6/KChartLeveyJenningsAxis.h
/usr/include/KChart6/KChartLeveyJenningsCoordinatePlane
/usr/include/KChart6/KChartLeveyJenningsCoordinatePlane.h
/usr/include/KChart6/KChartLeveyJenningsDiagram
/usr/include/KChart6/KChartLeveyJenningsDiagram.h
/usr/include/KChart6/KChartLeveyJenningsGridAttributes
/usr/include/KChart6/KChartLeveyJenningsGridAttributes.h
/usr/include/KChart6/KChartLineAttributes
/usr/include/KChart6/KChartLineAttributes.h
/usr/include/KChart6/KChartLineDiagram
/usr/include/KChart6/KChartLineDiagram.h
/usr/include/KChart6/KChartMarkerAttributes
/usr/include/KChart6/KChartMarkerAttributes.h
/usr/include/KChart6/KChartMeasure
/usr/include/KChart6/KChartMeasure.h
/usr/include/KChart6/KChartPaintContext
/usr/include/KChart6/KChartPaintContext.h
/usr/include/KChart6/KChartPalette
/usr/include/KChart6/KChartPalette.h
/usr/include/KChart6/KChartPieAttributes
/usr/include/KChart6/KChartPieAttributes.h
/usr/include/KChart6/KChartPieDiagram
/usr/include/KChart6/KChartPieDiagram.h
/usr/include/KChart6/KChartPlotter
/usr/include/KChart6/KChartPlotter.h
/usr/include/KChart6/KChartPolarCoordinatePlane
/usr/include/KChart6/KChartPolarCoordinatePlane.h
/usr/include/KChart6/KChartPolarDiagram
/usr/include/KChart6/KChartPolarDiagram.h
/usr/include/KChart6/KChartPosition
/usr/include/KChart6/KChartPosition.h
/usr/include/KChart6/KChartRadarCoordinatePlane
/usr/include/KChart6/KChartRadarCoordinatePlane.h
/usr/include/KChart6/KChartRadarDiagram
/usr/include/KChart6/KChartRadarDiagram.h
/usr/include/KChart6/KChartRelativePosition
/usr/include/KChart6/KChartRelativePosition.h
/usr/include/KChart6/KChartRingDiagram
/usr/include/KChart6/KChartRingDiagram.h
/usr/include/KChart6/KChartRulerAttributes
/usr/include/KChart6/KChartRulerAttributes.h
/usr/include/KChart6/KChartStockBarAttributes
/usr/include/KChart6/KChartStockBarAttributes.h
/usr/include/KChart6/KChartStockDiagram
/usr/include/KChart6/KChartStockDiagram.h
/usr/include/KChart6/KChartTernaryAxis
/usr/include/KChart6/KChartTernaryAxis.h
/usr/include/KChart6/KChartTernaryCoordinatePlane
/usr/include/KChart6/KChartTernaryCoordinatePlane.h
/usr/include/KChart6/KChartTernaryLineDiagram
/usr/include/KChart6/KChartTernaryLineDiagram.h
/usr/include/KChart6/KChartTernaryPointDiagram
/usr/include/KChart6/KChartTernaryPointDiagram.h
/usr/include/KChart6/KChartTextArea
/usr/include/KChart6/KChartTextArea.h
/usr/include/KChart6/KChartTextAttributes
/usr/include/KChart6/KChartTextAttributes.h
/usr/include/KChart6/KChartThreeDBarAttributes
/usr/include/KChart6/KChartThreeDBarAttributes.h
/usr/include/KChart6/KChartThreeDLineAttributes
/usr/include/KChart6/KChartThreeDLineAttributes.h
/usr/include/KChart6/KChartThreeDPieAttributes
/usr/include/KChart6/KChartThreeDPieAttributes.h
/usr/include/KChart6/KChartValueTrackerAttributes
/usr/include/KChart6/KChartValueTrackerAttributes.h
/usr/include/KChart6/KChartWidget
/usr/include/KChart6/KChartWidget.h
/usr/include/KChart6/kchart_export.h
/usr/include/KChart6/kchart_version.h
/usr/include/KGantt6/KGanttAbstractGrid
/usr/include/KGantt6/KGanttAbstractRowController
/usr/include/KGantt6/KGanttConstraint
/usr/include/KGantt6/KGanttConstraintGraphicsItem
/usr/include/KGantt6/KGanttConstraintModel
/usr/include/KGantt6/KGanttConstraintProxy
/usr/include/KGantt6/KGanttDateTimeGrid
/usr/include/KGantt6/KGanttDateTimeTimeLine
/usr/include/KGantt6/KGanttDateTimeTimeLineDialog
/usr/include/KGantt6/KGanttForwardingProxyModel
/usr/include/KGantt6/KGanttGlobal
/usr/include/KGantt6/KGanttGraphicsItem
/usr/include/KGantt6/KGanttGraphicsScene
/usr/include/KGantt6/KGanttGraphicsView
/usr/include/KGantt6/KGanttItemDelegate
/usr/include/KGantt6/KGanttLegend
/usr/include/KGantt6/KGanttListViewRowController
/usr/include/KGantt6/KGanttPenStyleComboBox
/usr/include/KGantt6/KGanttPrintingContext
/usr/include/KGantt6/KGanttProxyModel
/usr/include/KGantt6/KGanttStyleOptionGanttItem
/usr/include/KGantt6/KGanttSummaryHandlingProxyModel
/usr/include/KGantt6/KGanttTreeViewRowController
/usr/include/KGantt6/KGanttView
/usr/include/KGantt6/kgantt_export.h
/usr/include/KGantt6/kgantt_version.h
/usr/include/KGantt6/kganttabstractgrid.h
/usr/include/KGantt6/kganttabstractgrid_p.h
/usr/include/KGantt6/kganttabstractrowcontroller.h
/usr/include/KGantt6/kganttconstraint.h
/usr/include/KGantt6/kganttconstraintgraphicsitem.h
/usr/include/KGantt6/kganttconstraintmodel.h
/usr/include/KGantt6/kganttconstraintproxy.h
/usr/include/KGantt6/kganttdatetimegrid.h
/usr/include/KGantt6/kganttdatetimetimeline.h
/usr/include/KGantt6/kganttdatetimetimelinedialog.h
/usr/include/KGantt6/kganttforwardingproxymodel.h
/usr/include/KGantt6/kganttglobal.h
/usr/include/KGantt6/kganttgraphicsitem.h
/usr/include/KGantt6/kganttgraphicsscene.h
/usr/include/KGantt6/kganttgraphicsview.h
/usr/include/KGantt6/kganttitemdelegate.h
/usr/include/KGantt6/kganttlegend.h
/usr/include/KGantt6/kganttlistviewrowcontroller.h
/usr/include/KGantt6/kganttpenstylecombobox.h
/usr/include/KGantt6/kganttprintingcontext.h
/usr/include/KGantt6/kganttproxymodel.h
/usr/include/KGantt6/kganttstyleoptionganttitem.h
/usr/include/KGantt6/kganttsummaryhandlingproxymodel.h
/usr/include/KGantt6/kgantttreeviewrowcontroller.h
/usr/include/KGantt6/kganttview.h
/usr/lib64/cmake/KChart6/KChart6Config.cmake
/usr/lib64/cmake/KChart6/KChart6ConfigVersion.cmake
/usr/lib64/cmake/KChart6/KChart6Targets-relwithdebinfo.cmake
/usr/lib64/cmake/KChart6/KChart6Targets.cmake
/usr/lib64/cmake/KGantt6/KGantt6Config.cmake
/usr/lib64/cmake/KGantt6/KGantt6ConfigVersion.cmake
/usr/lib64/cmake/KGantt6/KGantt6Targets-relwithdebinfo.cmake
/usr/lib64/cmake/KGantt6/KGantt6Targets.cmake
/usr/lib64/libKChart6.so
/usr/lib64/libKGantt6.so

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKChart6.so.3.0.1
/V3/usr/lib64/libKGantt6.so.3.0.1
/usr/lib64/libKChart6.so.3
/usr/lib64/libKChart6.so.3.0.1
/usr/lib64/libKGantt6.so.3
/usr/lib64/libKGantt6.so.3.0.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kdiagram/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/kdiagram/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/kdiagram/a4c60b3fefda228cd7439d3565df043192fef137
