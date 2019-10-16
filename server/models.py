from server import db


class Patient(db.Model):
    id = db.Column(db.String(20), primary_key=True)
    firstNames = db.Column(db.String(40))
    lastNames = db.Column(db.String(40))
    gender = db.Columns(db.String(8))
    dateOfBirth = db.Column(db.String(20))

    ehrId = db.Column(db.String(20))
    Personnummer = db.Column(db.String(13))

    pulse = db.Column(db.Integer)
    oxSaturation = db.Column(db.Integer)
    sysBloodPressure = db.Column(db.Integer)
    diaBloodPressure = db.Column(db.Integer)

    breathingFreq = db.column(db.Integer)
    alertness = db.column(db.String(10))
    bodyTemp = db.Column(db.Float)

    def serialize(self):
        return {
            'demographics': {
                'id': self.id,
                'firstNames': self.firstNames,
                'lastNames': self.lastNames,
                'gender': self.gender,
                'dateOfBirth': self.dateOfBirth,
                'additionalInfo': {
                    'ehrId': self.ehrId,
                    'Personnummer': self.Personnummer
                }
            },
            'vital_signs': {
                'body_temperature': [
                    {
                        'any_event': [
                            {
                                'temperature': [
                                    {
                                        '|magnitude': self.bodyTemp,
                                        '|unit': '°C'
                                    }
                                ]
                            }
                        ]
                    }
                ],
                'blood_pressure': [
                    {
                        'any_event': [
                            {
                                'systolic': [
                                    {
                                        '|unit': 'mm[Hg]',
                                        '|magnitude': self.sysBloodPressure
                                    }
                                ],
                                'diastolic': [
                                    {
                                        '|unit': 'mm[Hg]',
                                        '|magnitude': self.diaBloodPressure
                                    }
                                ],
                                'position': [
                                    {
                                        '|code': 'at1001',
                                        '|value': 'Sitting'
                                    }
                                ]
                            }
                        ]
                    }
                ]
            },
            'pulse': self.pulse,
            'oxygen_Saturation': self.oxSaturation,
            'breathing_Frequency': self.breathingFreq,
            'alertness': self.alertness
        }

    def short_form(self):
        return {
            'pid': self.Personnummer,
            'firstNames': self.firstNames,
            'lastNames': self.lastNames
        }