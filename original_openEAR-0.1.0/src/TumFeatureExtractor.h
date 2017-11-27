/*******************************************************************************
 * openSMILE
 *  - open Speech and Music Interpretation by Large-space Extraction -
 * Copyright (C) 2008  Florian Eyben, Martin Woellmer, Bjoern Schuller
 * 
 * Institute for Human-Machine Communication
 * Technische Universitaet Muenchen (TUM)
 * D-80333 Munich, Germany
 *
 * If you use openSMILE or any code from openSMILE in your research work,
 * you are kindly asked to acknowledge the use of openSMILE in your publications.
 * See the file CITING.txt for details.
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
 *******************************************************************************/

/*
 *  TumFeatureExtractor.h
 *  semaine
 *  
 */

#ifndef SEMAINE_COMPONENTS_SMILE_TUMFEATUREEXTRACTOR_H
#define SEMAINE_COMPONENTS_SMILE_TUMFEATUREEXTRACTOR_H

#include <semaine/config.h>

#include <cms/CMSException.h>

#include <semaine/components/Component.h>
#include <semaine/cms/sender/FeatureSender.h>
//#include <semaine/cms/receiver/FeatureReceiver.h>
#include <semaine/cms/sender/EmmaSender.h>

#include <smileCommon.hpp>

#include <configManager.hpp>
#include <commandlineParser.hpp>
#include <componentManager.hpp>

#include <semaineComponentForSmile.hpp>

/*** class definition ***/

//using namespace opensmile;
using namespace cms;
using namespace semaine::components;
//using namespace tum::components:smile;
using namespace semaine::cms::sender;

namespace semaine {
namespace components {
namespace smile {

class TumFeatureExtractor : public ComponentForSmile
{
public:
	TumFeatureExtractor(cComponentManager *_cMan, cConfigManager *_conf) throw (CMSException);
 
	virtual ~TumFeatureExtractor();

protected:
	virtual void act() throw (CMSException);
        virtual void react(SEMAINEMessage * message) throw (std::exception);
	virtual void customStartIO() throw (CMSException);

private:
	FeatureSender * featureSender;
//	FeatureReceiver * featureReceiver;
	EmmaSender * emmaSender;

	smileThread smileMainThread;
};


//#endif

} // namespace smile
} // namespace components
} // namespace semaine


#endif

