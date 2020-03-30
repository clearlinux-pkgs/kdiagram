#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : kdiagram
Version  : 2.6.2
Release  : 3
URL      : https://github.com/KDE/kdiagram/archive/v2.6.2/kdiagram-2.6.2.tar.gz
Source0  : https://github.com/KDE/kdiagram/archive/v2.6.2/kdiagram-2.6.2.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: kdiagram-lib = %{version}-%{release}
Requires: kdiagram-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde

%description
Running the examples
The examples are only compiled automatically if you pass the -unittests option
to configure. This is because some examples require the "testtools" internal
library that is not installed when configured without -unittests.

%package dev
Summary: dev components for the kdiagram package.
Group: Development
Requires: kdiagram-lib = %{version}-%{release}
Provides: kdiagram-devel = %{version}-%{release}
Requires: kdiagram = %{version}-%{release}

%description dev
dev components for the kdiagram package.


%package lib
Summary: lib components for the kdiagram package.
Group: Libraries
Requires: kdiagram-license = %{version}-%{release}

%description lib
lib components for the kdiagram package.


%package license
Summary: license components for the kdiagram package.
Group: Default

%description license
license components for the kdiagram package.


%prep
%setup -q -n kdiagram-2.6.2
cd %{_builddir}/kdiagram-2.6.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1585589237
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1585589237
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kdiagram
cp %{_builddir}/kdiagram-2.6.2/LICENSE.GPL.txt %{buildroot}/usr/share/package-licenses/kdiagram/4cc77b90af91e615a64ae04893fdffa7939db84c
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/KChart/KChart
/usr/include/KChart/KChartAbstractArea
/usr/include/KChart/KChartAbstractArea.h
/usr/include/KChart/KChartAbstractAreaBase
/usr/include/KChart/KChartAbstractAreaBase.h
/usr/include/KChart/KChartAbstractAreaWidget
/usr/include/KChart/KChartAbstractAreaWidget.h
/usr/include/KChart/KChartAbstractAxis
/usr/include/KChart/KChartAbstractAxis.h
/usr/include/KChart/KChartAbstractCartesianDiagram
/usr/include/KChart/KChartAbstractCartesianDiagram.h
/usr/include/KChart/KChartAbstractCoordinatePlane
/usr/include/KChart/KChartAbstractCoordinatePlane.h
/usr/include/KChart/KChartAbstractDiagram
/usr/include/KChart/KChartAbstractDiagram.h
/usr/include/KChart/KChartAbstractPieDiagram
/usr/include/KChart/KChartAbstractPieDiagram.h
/usr/include/KChart/KChartAbstractPolarDiagram
/usr/include/KChart/KChartAbstractPolarDiagram.h
/usr/include/KChart/KChartAbstractProxyModel
/usr/include/KChart/KChartAbstractProxyModel.h
/usr/include/KChart/KChartAbstractTernaryDiagram
/usr/include/KChart/KChartAbstractTernaryDiagram.h
/usr/include/KChart/KChartAbstractThreeDAttributes
/usr/include/KChart/KChartAbstractThreeDAttributes.h
/usr/include/KChart/KChartAttributesModel
/usr/include/KChart/KChartAttributesModel.h
/usr/include/KChart/KChartBackgroundAttributes
/usr/include/KChart/KChartBackgroundAttributes.h
/usr/include/KChart/KChartBarAttributes
/usr/include/KChart/KChartBarAttributes.h
/usr/include/KChart/KChartBarDiagram
/usr/include/KChart/KChartBarDiagram.h
/usr/include/KChart/KChartCartesianAxis
/usr/include/KChart/KChartCartesianAxis.h
/usr/include/KChart/KChartCartesianCoordinatePlane
/usr/include/KChart/KChartCartesianCoordinatePlane.h
/usr/include/KChart/KChartChart
/usr/include/KChart/KChartChart.h
/usr/include/KChart/KChartDataValueAttributes
/usr/include/KChart/KChartDataValueAttributes.h
/usr/include/KChart/KChartDatasetProxyModel
/usr/include/KChart/KChartDatasetProxyModel.h
/usr/include/KChart/KChartDatasetSelector
/usr/include/KChart/KChartDatasetSelector.h
/usr/include/KChart/KChartDiagramObserver
/usr/include/KChart/KChartDiagramObserver.h
/usr/include/KChart/KChartEnums
/usr/include/KChart/KChartEnums.h
/usr/include/KChart/KChartFrameAttributes
/usr/include/KChart/KChartFrameAttributes.h
/usr/include/KChart/KChartGlobal
/usr/include/KChart/KChartGlobal.h
/usr/include/KChart/KChartGridAttributes
/usr/include/KChart/KChartGridAttributes.h
/usr/include/KChart/KChartHeaderFooter
/usr/include/KChart/KChartHeaderFooter.h
/usr/include/KChart/KChartLayoutItems
/usr/include/KChart/KChartLayoutItems.h
/usr/include/KChart/KChartLegend
/usr/include/KChart/KChartLegend.h
/usr/include/KChart/KChartLeveyJenningsAxis
/usr/include/KChart/KChartLeveyJenningsAxis.h
/usr/include/KChart/KChartLeveyJenningsCoordinatePlane
/usr/include/KChart/KChartLeveyJenningsCoordinatePlane.h
/usr/include/KChart/KChartLeveyJenningsDiagram
/usr/include/KChart/KChartLeveyJenningsDiagram.h
/usr/include/KChart/KChartLeveyJenningsGridAttributes
/usr/include/KChart/KChartLeveyJenningsGridAttributes.h
/usr/include/KChart/KChartLineAttributes
/usr/include/KChart/KChartLineAttributes.h
/usr/include/KChart/KChartLineDiagram
/usr/include/KChart/KChartLineDiagram.h
/usr/include/KChart/KChartMarkerAttributes
/usr/include/KChart/KChartMarkerAttributes.h
/usr/include/KChart/KChartMeasure
/usr/include/KChart/KChartMeasure.h
/usr/include/KChart/KChartPaintContext
/usr/include/KChart/KChartPaintContext.h
/usr/include/KChart/KChartPalette
/usr/include/KChart/KChartPalette.h
/usr/include/KChart/KChartPieAttributes
/usr/include/KChart/KChartPieAttributes.h
/usr/include/KChart/KChartPieDiagram
/usr/include/KChart/KChartPieDiagram.h
/usr/include/KChart/KChartPlotter
/usr/include/KChart/KChartPlotter.h
/usr/include/KChart/KChartPolarCoordinatePlane
/usr/include/KChart/KChartPolarCoordinatePlane.h
/usr/include/KChart/KChartPolarDiagram
/usr/include/KChart/KChartPolarDiagram.h
/usr/include/KChart/KChartPosition
/usr/include/KChart/KChartPosition.h
/usr/include/KChart/KChartRadarCoordinatePlane
/usr/include/KChart/KChartRadarCoordinatePlane.h
/usr/include/KChart/KChartRadarDiagram
/usr/include/KChart/KChartRadarDiagram.h
/usr/include/KChart/KChartRelativePosition
/usr/include/KChart/KChartRelativePosition.h
/usr/include/KChart/KChartRingDiagram
/usr/include/KChart/KChartRingDiagram.h
/usr/include/KChart/KChartRulerAttributes
/usr/include/KChart/KChartRulerAttributes.h
/usr/include/KChart/KChartStockBarAttributes
/usr/include/KChart/KChartStockBarAttributes.h
/usr/include/KChart/KChartStockDiagram
/usr/include/KChart/KChartStockDiagram.h
/usr/include/KChart/KChartTernaryAxis
/usr/include/KChart/KChartTernaryAxis.h
/usr/include/KChart/KChartTernaryCoordinatePlane
/usr/include/KChart/KChartTernaryCoordinatePlane.h
/usr/include/KChart/KChartTernaryLineDiagram
/usr/include/KChart/KChartTernaryLineDiagram.h
/usr/include/KChart/KChartTernaryPointDiagram
/usr/include/KChart/KChartTernaryPointDiagram.h
/usr/include/KChart/KChartTextArea
/usr/include/KChart/KChartTextArea.h
/usr/include/KChart/KChartTextAttributes
/usr/include/KChart/KChartTextAttributes.h
/usr/include/KChart/KChartThreeDBarAttributes
/usr/include/KChart/KChartThreeDBarAttributes.h
/usr/include/KChart/KChartThreeDLineAttributes
/usr/include/KChart/KChartThreeDLineAttributes.h
/usr/include/KChart/KChartThreeDPieAttributes
/usr/include/KChart/KChartThreeDPieAttributes.h
/usr/include/KChart/KChartValueTrackerAttributes
/usr/include/KChart/KChartValueTrackerAttributes.h
/usr/include/KChart/KChartWidget
/usr/include/KChart/KChartWidget.h
/usr/include/KChart/kchart_export.h
/usr/include/KGantt/KGanttAbstractGrid
/usr/include/KGantt/KGanttAbstractRowController
/usr/include/KGantt/KGanttConstraint
/usr/include/KGantt/KGanttConstraintGraphicsItem
/usr/include/KGantt/KGanttConstraintModel
/usr/include/KGantt/KGanttConstraintProxy
/usr/include/KGantt/KGanttDateTimeGrid
/usr/include/KGantt/KGanttForwardingProxyModel
/usr/include/KGantt/KGanttGlobal
/usr/include/KGantt/KGanttGraphicsItem
/usr/include/KGantt/KGanttGraphicsScene
/usr/include/KGantt/KGanttGraphicsView
/usr/include/KGantt/KGanttItemDelegate
/usr/include/KGantt/KGanttLegend
/usr/include/KGantt/KGanttListViewRowController
/usr/include/KGantt/KGanttProxyModel
/usr/include/KGantt/KGanttStyleOptionGanttItem
/usr/include/KGantt/KGanttSummaryHandlingProxyModel
/usr/include/KGantt/KGanttTreeViewRowController
/usr/include/KGantt/KGanttView
/usr/include/KGantt/kgantt_export.h
/usr/include/KGantt/kganttabstractgrid.h
/usr/include/KGantt/kganttabstractrowcontroller.h
/usr/include/KGantt/kganttconstraint.h
/usr/include/KGantt/kganttconstraintgraphicsitem.h
/usr/include/KGantt/kganttconstraintmodel.h
/usr/include/KGantt/kganttconstraintproxy.h
/usr/include/KGantt/kganttdatetimegrid.h
/usr/include/KGantt/kganttforwardingproxymodel.h
/usr/include/KGantt/kganttglobal.h
/usr/include/KGantt/kganttgraphicsitem.h
/usr/include/KGantt/kganttgraphicsscene.h
/usr/include/KGantt/kganttgraphicsview.h
/usr/include/KGantt/kganttitemdelegate.h
/usr/include/KGantt/kganttlegend.h
/usr/include/KGantt/kganttlistviewrowcontroller.h
/usr/include/KGantt/kganttproxymodel.h
/usr/include/KGantt/kganttstyleoptionganttitem.h
/usr/include/KGantt/kganttsummaryhandlingproxymodel.h
/usr/include/KGantt/kgantttreeviewrowcontroller.h
/usr/include/KGantt/kganttview.h
/usr/include/kchart_version.h
/usr/include/kgantt_version.h
/usr/lib64/cmake/KChart/KChartConfig.cmake
/usr/lib64/cmake/KChart/KChartConfigVersion.cmake
/usr/lib64/cmake/KChart/KChartTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KChart/KChartTargets.cmake
/usr/lib64/cmake/KGantt/KGanttConfig.cmake
/usr/lib64/cmake/KGantt/KGanttConfigVersion.cmake
/usr/lib64/cmake/KGantt/KGanttTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KGantt/KGanttTargets.cmake
/usr/lib64/libKChart.so
/usr/lib64/libKGantt.so
/usr/lib64/qt5/mkspecs/modules/qt_KChart.pri
/usr/lib64/qt5/mkspecs/modules/qt_KGantt.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKChart.so.2
/usr/lib64/libKChart.so.2.6.2
/usr/lib64/libKGantt.so.2
/usr/lib64/libKGantt.so.2.6.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kdiagram/4cc77b90af91e615a64ae04893fdffa7939db84c
