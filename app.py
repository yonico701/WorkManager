from flask import Flask, jsonify, request
from services.System import System
import services.customer_service as customer_service
import services.provider_service as provider_service
import services.job_service as job_service





app = Flask(__name__)
system = System()
system.load_all_data()

@app.route('/')
def hello_world():
    return 'WorkManager api is running'


### customers routes ###


@app.route('/customers')
def get_customers():
    try:
        customers = customer_service.get_all_customers()

        customers_json = []
        for customer in customers:
            customers_json.append(customer.to_dict())

        return jsonify(customers_json), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/customers', methods=['POST'])
def create_customer():
    try:
        data = request.get_json()
        customer = customer_service.create_customer(data)

        return jsonify({
            "message": "customer created successfully",
            "customer": customer.to_dict()
        }), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/customers/<customer_id>', methods=['GET'])
def get_customer(customer_id):
    try:

        customer = customer_service.get_customer_by_id(customer_id)

        if customer is None:
            return jsonify({'error': 'customer not found'}), 404

        return jsonify(customer.to_dict()), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 400




@app.route('/customers/<customer_id>/jobs', methods=['GET'])
def get_jobs_by_customer(customer_id):
    try:
        customer_jobs = customer_service.get_jobs_by_customer(customer_id)

        customer_jobs_json = []
        for job in customer_jobs:
            customer_jobs_json.append(job.to_dict())

        return jsonify(customer_jobs_json), 200

    except ValueError as e:
        return jsonify({'error': str(e)}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 400




@app.route('/customers/<customer_id>/address', methods=['PATCH'])
def update_customer_address(customer_id):
    try:

        data = request.get_json()

        customer = customer_service.update_customer_address(
            customer_id,
            data['address']
        )

        return jsonify({
            "message": "customer address updated successfully",
            "customer": customer.to_dict()
        }), 200

    except ValueError as e:
        return jsonify({'error': str(e)}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/customers/<customer_id>/notes', methods=['PATCH'])
def update_customer_notes(customer_id):
    try:

        data = request.get_json()

        customer = customer_service.update_customer_notes(
            customer_id,
            data['notes']
        )

        return jsonify({
            "message": "customer notes updated successfully",
            "customer": customer.to_dict()
        }), 200

    except ValueError as e:
        return jsonify({'error': str(e)}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 400



@app.route('/customers/<customer_id>/notes', methods=['DELETE'])
def delete_customer_notes(customer_id):
    try:
        customer = customer_service.delete_customer_notes(customer_id)

        return jsonify({
            "message": "customer notes deleted successfully",
            "customer": customer.to_dict()
        }), 200

    except ValueError as e:
        return jsonify({'error': str(e)}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/customers/<customer_id>/activate', methods=['PATCH'])
def activate_customer(customer_id):
    try:
        customer = customer_service.activate_customer(customer_id)

        return jsonify({
            "message": "customer activated successfully",
            "customer": customer.to_dict()
        }), 200

    except ValueError as e:
        return jsonify({'error': str(e)}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/customers/<customer_id>/deactivate', methods=['PATCH'])
def deactivate_customer(customer_id):
    try:
        customer = customer_service.deactivate_customer(customer_id)

        return jsonify({
            "message": "customer deactivated successfully",
            "customer": customer.to_dict()
        }), 200

    except ValueError as e:
        return jsonify({'error': str(e)}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 400

### providers ###

@app.route('/providers')
def get_providers():
    try:
        providers = provider_service.get_all_providers()

        providers_json = []
        for provider in providers:
            providers_json.append(provider.to_dict())

        return jsonify(providers_json), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/providers/<provider_id>/jobs', methods=['GET'])
def get_jobs_by_provider(provider_id):
    try:
        provider_jobs = provider_service.get_jobs_by_provider(provider_id)

        provider_jobs_json = []
        for job in provider_jobs:
            provider_jobs_json.append(job.to_dict())

        return jsonify(provider_jobs_json), 200

    except ValueError as e:
        return jsonify({'error': str(e)}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/providers', methods=['POST'])
def create_provider():
    try:
        data = request.get_json()

        provider = provider_service.create_provider(data)

        return jsonify({
            "message": "provider created successfully",
            "provider": provider.to_dict()
        }), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/providers/<provider_id>', methods=['GET'])
def get_provider(provider_id):
    try:
        provider = provider_service.get_provider_by_id(provider_id)

        if provider is None:
            return jsonify({'error': 'provider not found'}), 404

        return jsonify(provider.to_dict()), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/providers/<provider_id>/base_price', methods=['PATCH'])
def update_provider_base_price(provider_id):
    try:
        data = request.get_json()

        provider = provider_service.update_provider_base_price(
            provider_id,
            data['base_price']
        )

        return jsonify({
            "message": "base price updated successfully",
            "provider": provider.to_dict()
        }), 200

    except ValueError as e:
        return jsonify({'error': str(e)}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/providers/<provider_id>/profession', methods=['PATCH'])
def add_provider_profession(provider_id):
    try:
        data = request.get_json()

        provider = provider_service.add_provider_profession(
            provider_id,
            data['profession']
        )

        return jsonify({
            "message": "profession updated successfully",
            "provider": provider.to_dict()
        }), 200

    except ValueError as e:
        return jsonify({'error': str(e)}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/providers/<provider_id>/availability', methods=['PATCH'])
def update_provider_availability(provider_id):
    try:
        provider = provider_service.mark_provider_availability(provider_id)

        return jsonify({
            "message": "availability updated successfully",
            "provider": provider.to_dict()
        }), 200

    except ValueError as e:
        return jsonify({'error': str(e)}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/providers/<provider_id>/unavailability', methods=['PATCH'])
def update_provider_unavailability(provider_id):
    try:
        provider = provider_service.mark_provider_unavailability(provider_id)

        return jsonify({
            "message": "unavailability updated successfully",
            "provider": provider.to_dict()
        }), 200

    except ValueError as e:
        return jsonify({'error': str(e)}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/providers/<provider_id>/activate', methods=['PATCH'])
def activate_provider(provider_id):
    try:
        provider = provider_service.activate_provider(provider_id)

        return jsonify({
            "message": "provider activated successfully",
            "provider": provider.to_dict()
        }), 200

    except ValueError as e:
        return jsonify({'error': str(e)}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/providers/<provider_id>/deactivate', methods=['PATCH'])
def deactivate_provider(provider_id):
    try:
        provider = provider_service.deactivate_provider(provider_id)

        return jsonify({
            "message": "provider deactivated successfully",
            "provider": provider.to_dict()
        }), 200

    except ValueError as e:
        return jsonify({'error': str(e)}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 400

### jobs ###

@app.route('/jobs', methods=['GET'])
def get_jobs():
    try:

        status = request.args.get('status')

        jobs = job_service.get_all_jobs(status)

        jobs_to_dict = []

        for job in jobs:
            jobs_to_dict.append(job.to_dict())

        return jsonify({"jobs": jobs_to_dict}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/jobs', methods=['POST'])
def create_job():
    try:

        data = request.get_json()

        new_job = job_service.create_job(data)

        return jsonify({
            "message": "job created successfully",
            "job": new_job.to_dict()
        }), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/jobs/<job_id>/assign/<provider_id>', methods=['POST'])
def assign_provider_to_job(job_id, provider_id):
    try:

        job = job_service.assign_provider_to_job(
            job_id,
            provider_id
        )

        return jsonify({
            "message": "job assigned successfully",
            "job": job.to_dict()
        }), 200

    except ValueError as e:
        return jsonify({'error': str(e)}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/jobs/<job_id>/start', methods=['POST'])
def start_job(job_id):
    try:

        job = job_service.start_job(job_id)

        return jsonify({
            "message": "job started successfully",
            "job": job.to_dict()
        }), 200

    except ValueError as e:
        return jsonify({'error': str(e)}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/jobs/<job_id>/complete', methods=['POST'])
def complete_job(job_id):
    try:

        job = job_service.complete_job(job_id)

        return jsonify({
            "message": "job completed successfully",
            "job": job.to_dict()
        }), 200

    except ValueError as e:
        return jsonify({'error': str(e)}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/jobs/<job_id>/cancel', methods=['POST'])
def cancel_job(job_id):
    try:

        job = job_service.cancel_job(job_id)

        return jsonify({
            "message": "job canceled successfully",
            "job": job.to_dict()
        }), 200

    except ValueError as e:
        return jsonify({'error': str(e)}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/jobs/<job_id>/price', methods=['PATCH'])
def update_job_price(job_id):
    try:

        data = request.get_json()

        job = job_service.update_job_price(
            job_id,
            data['price']
        )

        return jsonify({
            "message": "job price updated successfully",
            "job": job.to_dict()
        }), 200

    except ValueError as e:
        return jsonify({'error': str(e)}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/jobs/<job_id>/address', methods=['PATCH'])
def update_job_address(job_id):
    try:

        data = request.get_json()

        job = job_service.update_job_address(
            job_id,
            data['address']
        )

        return jsonify({
            "message": "address job updated successfully",
            "job": job.to_dict()
        }), 200

    except ValueError as e:
        return jsonify({'error': str(e)}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/jobs/<job_id>/description', methods=['PATCH'])
def update_job_description(job_id):
    try:

        data = request.get_json()

        job = job_service.update_job_description(
            job_id,
            data['description']
        )

        return jsonify({
            "message": "description job updated successfully",
            "job": job.to_dict()
        }), 200

    except ValueError as e:
        return jsonify({'error': str(e)}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/jobs/<job_id>/schedule', methods=['PATCH'])
def update_job_schedule(job_id):
    try:

        data = request.get_json()

        job = job_service.update_job_schedule(
            job_id,
            data['schedule_date']
        )

        return jsonify({
            "message": "schedule job updated successfully",
            "job": job.to_dict()
        }), 200

    except ValueError as e:
        return jsonify({'error': str(e)}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 400




if __name__ == '__main__':
    app.run()