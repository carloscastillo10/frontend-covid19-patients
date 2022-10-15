from app.dashboard import blueprint, controller as dashboard_controller
from flask import abort, jsonify, redirect, render_template, request


@blueprint.route('/')
def index():
    try:
        return render_template('home/dashboard.html', segment='dashboard', page_name='Dashboard')
    except Exception:
        abort(500)


@blueprint.route('/dashboard')
@blueprint.route('/index')
def dashboard():
    return redirect('/')


@blueprint.route('/initial-dashboard-data')
def get_initial_dashboard_data():
    try:
        data = {
            "weekly_ranking": {
                "start_date": "10/06/2022",
                "end_date": "10/13/2022",
                "labels": ["01 sep", "02 sep", "03 sep", "04 sep", "05 sep", "06 sep", "07 sep"],
                "data": {
                    "moderate_patients": {
                        "label": "Pacientes Moderados",
                        "data": [10, 7, 5, 7, 5, 5, 5],
                        "total": 42,
                        "percentage": 10,
                        "percentage_label": "desde la semana pasada"
                    },
                    "serius_patients": {
                        "label": "Pacientes Graves",
                        "data": [3, 3, 3, 5, 3, 3, 3],
                        "total": 23,
                        "percentage": 5,
                        "percentage_label": "desde la semana pasada"
                    },
                    "critical_patients": {
                        "label": "Pacientes Críticos",
                        "data": [3, 3, 3, 5, 3, 3, 3],
                        "total": 20,
                        "percentage": -20,
                        "percentage_label": "desde la semana pasada"
                    }
                }
            },
            "annual_ranking": {
                "labels": ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre"],
                "data": {
                    "moderate_patients": {
                        "label": "Pacientes Moderados",
                        "data": [50, 40, 300, 220, 500, 250, 400, 30, 100],
                    },
                    "serius_patients": {
                        "label": "Pacientes Graves",
                        "data": [30, 90, 40, 140, 290, 290, 340, 90, 50],
                    },
                    "critical_patients": {
                        "label": "Pacientes Críticos",
                        "data": [40, 80, 70, 90, 30, 90, 140, 80, 75],
                    }
                },
                "total": 150,
                "total_percentage": 20
            },
            "total_ranking": {
                "data": {
                    "moderate_patients": {
                        "label": "Pacientes Moderados",
                        "total": 140,
                    },
                    "serius_patients": {
                        "label": "Pacientes Graves",
                        "total": 60,
                    },
                    "critical_patients": {
                        "label": "Pacientes Críticos",
                        "total": 18,
                    }
                },
                "total": 218
            },
            "summary": {"patients": [
                {
                    "identification": "1101020304",
                    "name": "Andrés Manuel Ponce Perez",
                    "date": "24 Jul 2022",
                    "covid19_severity": "moderado",
                    "sato2": 95.6,
                    "pao2": 91.2,
                    "fio2": 30,
                    "pf_ratio": 304,
                    "respiratory_failure": False,
                    "ards": False,
                    "sepsis_shock": False,
                    "fever": True,
                    "cough": True,
                    "sore_throat": False,
                    "headache": False,
                    "fatigue": False,
                    "dyspnea": False,
                    "nausea": False,
                    "vomit": False,
                    "diarrhea": False,
                },
                {
                    "identification": "1102030405",
                    "name": "Amanda Maria Peña Torres",
                    "date": "24 Jul 2022",
                    "covid19_severity": "moderado",
                    "sato2": 94,
                    "pao2": 91.2,
                    "fio2": 30,
                    "pf_ratio": 304.7,
                    "respiratory_failure": False,
                    "ards": False,
                    "sepsis_shock": False,
                    "fever": True,
                    "cough": True,
                    "sore_throat": False,
                    "headache": False,
                    "fatigue": False,
                    "dyspnea": False,
                    "nausea": True,
                    "vomit": False,
                    "diarrhea": False,
                },
                {
                    "identification": "1103040506",
                    "name": "Tomás Andrés Torres Alban",
                    "date": "24 Jul 2022",
                    "covid19_severity": "grave",
                    "sato2": 92.2,
                    "pao2": 93.9,
                    "fio2": 45,
                    "pf_ratio": 208.7,
                    "respiratory_failure": False,
                    "ards": False,
                    "sepsis_shock": False,
                    "fever": True,
                    "cough": True,
                    "sore_throat": False,
                    "headache": False,
                    "fatigue": False,
                    "dyspnea": True,
                    "nausea": False,
                    "vomit": False,
                    "diarrhea": True,
                },
                {
                    "identification": "1104050607",
                    "name": "Jesús Alcivar Toledo Arteaga",
                    "date": "24 Jul 2022",
                    "covid19_severity": "moderado",
                    "sato2": 96.3,
                    "pao2": 89.2,
                    "fio2": 27,
                    "pf_ratio": 330.4,
                    "respiratory_failure": False,
                    "ards": False,
                    "sepsis_shock": False,
                    "fever": True,
                    "cough": True,
                    "sore_throat": False,
                    "headache": False,
                    "fatigue": False,
                    "dyspnea": True,
                    "nausea": False,
                    "vomit": False,
                    "diarrhea": False,
                },
                {
                    "identification": "1105060708",
                    "name": "Dolores María Gonza Quito",
                    "date": "23 Jul 2022",
                    "covid19_severity": "crítico",
                    "sato2": 91,
                    "pao2": 31.1,
                    "fio2": 15,
                    "pf_ratio": 207.3,
                    "respiratory_failure": True,
                    "ards": True,
                    "sepsis_shock": True,
                    "fever": True,
                    "cough": True,
                    "sore_throat": False,
                    "headache": True,
                    "fatigue": False,
                    "dyspnea": True,
                    "nausea": False,
                    "vomit": False,
                    "diarrhea": False,
                },
                {
                    "identification": "1101020304",
                    "name": "Andrés Manuel Ponce Perez",
                    "date": "24 Jul 2022",
                    "covid19_severity": "moderado",
                    "sato2": 95.6,
                    "pao2": 91.2,
                    "fio2": 30,
                    "pf_ratio": 304,
                    "respiratory_failure": False,
                    "ards": False,
                    "sepsis_shock": False,
                    "fever": True,
                    "cough": True,
                    "sore_throat": False,
                    "headache": False,
                    "fatigue": False,
                    "dyspnea": False,
                    "nausea": False,
                    "vomit": False,
                    "diarrhea": False,
                },
            ]}
        }

        # return jsonify(data)
        response = dashboard_controller.get_initial_data()
        return response.json(), response.status_code
    except Exception as e:
        abort(500, e)


@blueprint.route('/filter-patient-card')
def filter_patient_card():
    try:
        response = dashboard_controller.filter_data(request)
        return response.json(), response.status_code
        # return jsonify({"data": "ok"})
    except Exception as e:
        abort(500, e)


@blueprint.route('/filter-total-line-chart')
def filter_total_line_chart():
    dashboard_controller.filter_data(request)
    return jsonify({"data": "ok"})


@blueprint.route('/filter-summary-table')
def filter_summary_table():
    dashboard_controller.filter_data(request)
    return jsonify({"data": "ok"})
