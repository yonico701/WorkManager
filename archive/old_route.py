#
#
# @app.route('/customers', methods=['POST'])
# def create_customer():
#     try:
#         data = request.get_json()
#         customer = Customer(**data)
#
#         success = customer_repo.create_customer(customer)
        if not success:
            return jsonify({'error': 'customer creation failed'}), 400
        return jsonify(
            {"message": "customer created successfully",
             "customer": customer.to_dict()
             }), 201

    except Exception as e:
        return jsonify({'error': str(e)

                                 #
                                 #
                                 @ app.route('/customers')


def get_customers():
    try:
        customers = customer_repo.get_all_customers()
        customers_json = []
        for customer in customers:
            customers_json.append(customer.to_dict())
        return jsonify(customers_json), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


#
@app.route('/customers/<customer_id>', methods=['GET'])
def get_customer(customer_id):
    try:
        customer = customer_repo.get_customer_by_id(customer_id)
        if customer is None:
            return jsonify({'error': 'customer not found'}), 404
        return jsonify(customer.to_dict()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/customers/<customer_id>/jobs', methods=['GET'])
def get_jobs_by_customer(customer_id):
    try:
        customer_jobs_json = []

        customer = customer_repo.get_customer_by_id(customer_id)

        if customer is None:
            return jsonify({'error': 'customer not found'}), 404

        customer_jobs = job_repo.get_jobs_by_customer(customer_id)

        for job in customer_jobs:
            customer_jobs_json.append(job.to_dict())

        return jsonify(customer_jobs_json), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/customers/<customer_id>/address', methods=['PATCH'])
def update_customer_address(customer_id):
    try:
        customer = customer_repo.get_customer_by_id(customer_id)

        if customer is None:
            return jsonify({'error': 'customer not found'}), 404

        data = request.get_json()
        new_address = data['address']

        success = customer_repo.update_customer_address(customer_id, new_address)

        if not success:
            return jsonify({'error': 'customer address update failed'}), 400

        customer.address = new_address

        return jsonify({
            "message": "customer address updated successfully",
            "customer": customer.to_dict()
        }), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/customers/<customer_id>/notes', methods=['PATCH'])
def update_customer_notes(customer_id):
    try:
        customer = customer_repo.get_customer_by_id(customer_id)

        if customer is None:
            return jsonify({'error': 'customer not found'}), 404

        data = request.get_json()
        new_notes = data['notes']

        success = customer_repo.add_customer_notes(customer_id, new_notes)

        if not success:
            return jsonify({'error': 'customer notes update failed'}), 400

        customer.notes = new_notes

        return jsonify({
            "message": "customer notes updated successfully",
            "customer": customer.to_dict()
        }), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/customers/<customer_id>/notes', methods=['DELETE'])
def delete_customer_notes(customer_id):
    try:
        customer = customer_repo.get_customer_by_id(customer_id)
        if customer is None:
            return jsonify({'error': 'customer not found'}), 404
        success = customer_repo.remove_customer_notes(customer_id)
        if not success:
            return jsonify({'error': 'customer notes delete failed'}), 400
        customer.notes = ""
        return jsonify({"message": "customer notes deleted successfully",
                        "customer": customer.to_dict()}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/customers/<customer_id>/activate', methods=['PATCH'])
def activate_customer(customer_id):
    try:
        customer = customer_repo.get_customer_by_id(customer_id)

        if customer is None:
            return jsonify({'error': 'customer not found'}), 404

        success = customer_repo.activate_customer(customer_id)

        if not success:
            return jsonify({'error': 'customer activation failed'}), 400

        customer.active()

        return jsonify({"message": "customer activated successfully",
                        "customer": customer.to_dict()}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/customers/<customer_id>/deactivate', methods=['PATCH'])
def deactivate_customer(customer_id):
    try:
        customer = customer_repo.get_customer_by_id(customer_id)

        if customer is None:
            return jsonify({'error': 'customer not found'}), 404

        success = customer_repo.deactivate_customer(customer_id)

        if not success:
            return jsonify({'error': 'customer deactivation failed'}), 400

        customer.inactive()

        return jsonify({"message": "customer deactivated successfully",
                        "customer": customer.to_dict()}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 400


### providers ###

@app.route('/providers')
def get_providers():
    try:
        providers = provider_repo.get_all_providers()
        providers_json = []
        for provider in providers:
            providers_json.append(provider.to_dict())
        return jsonify(providers_json), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/providers/<provider_id>/jobs', methods=['GET'])
def get_jobs_by_provider(provider_id):
    try:
        provider_jobs_json = []
        provider = provider_repo.get_provider_by_id(provider_id)
        if provider is None:
            return jsonify({'error': 'provider not found'}), 404
        provider_jobs = job_repo.get_jobs_by_provider(provider_id)
        for job in provider_jobs:
            provider_jobs_json.append(job.to_dict())
        return jsonify(provider_jobs_json), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/providers', methods=['POST'])
def create_provider():
    try:
        data = request.get_json()
        provider = ServiceProvider(**data)
        success = provider_repo.create_provider(provider)
        if not success:
            return jsonify({'error': 'provider creation failed'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    return jsonify(
        {"message": "provider created successfully",
         "provider": provider.to_dict()
         }), 201


@app.route('/providers/<provider_id>', methods=['GET'])
def get_provider(provider_id):
    try:
        provider = provider_repo.get_provider_by_id(provider_id)
        if provider is None:
            return jsonify({'error': 'provider not found'}), 404
        return jsonify(provider.to_dict()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/providers/<provider_id>/base_price', methods=['PATCH'])
def update_provider_base_price(provider_id):
    try:
        data = request.get_json()
        provider = provider_repo.get_provider_by_id(provider_id)
        if provider is None:
            return jsonify({'error': 'provider not found'}), 404
        new_base_price = data['base_price']
        success = provider_repo.update_provider_base_price(provider_id, new_base_price)
        if not success:
            return jsonify({'error': 'provider base price update failed'}), 400
        provider = provider_repo.get_provider_by_id(provider_id)
        return jsonify({"message": "base price updated successfully",
                        "provider": provider.to_dict()}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/providers/<provider_id>/profession', methods=['PATCH'])
def add_provider_profession(provider_id):
    try:
        data = request.get_json()
        provider = provider_repo.get_provider_by_id(provider_id)
        if provider is None:
            return jsonify({'error': 'provider not found'}), 404
        new_profession = data['profession']
        success = provider_repo.add_provider_profession(provider_id, new_profession)
        if not success:
            return jsonify({'error': 'provider profession update failed'}), 400
        provider = provider_repo.get_provider_by_id(provider_id)
        return jsonify({"message": "profession updated successfully",
                        "provider": provider.to_dict()}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/providers/<provider_id>/availability', methods=['PATCH'])
def update_provider_availability(provider_id):
    try:
        provider = provider_repo.get_provider_by_id(provider_id)
        if provider is None:
            return jsonify({'error': 'provider not found'}), 404
        success = provider_repo.mark_provider_availability(provider_id)
        if not success:
            return jsonify({'error': 'provider availability update failed'}), 400
        provider = provider_repo.get_provider_by_id(provider_id)
        return jsonify({"message": "availability updated successfully",
                        "provider": provider.to_dict()}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/providers/<provider_id>/unavailability', methods=['PATCH'])
def update_provider_unavailability(provider_id):
    try:
        provider = provider_repo.get_provider_by_id(provider_id)
        if provider is None:
            return jsonify({'error': 'provider not found'}), 404
        success = provider_repo.mark_provider_unavailability(provider_id)
        if not success:
            return jsonify({'error': 'provider unavailability update failed'}), 400
        provider = provider_repo.get_provider_by_id(provider_id)
        return jsonify({"message": "unavailability updated successfully",
                        "provider": provider.to_dict()}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/providers/<provider_id>/activate', methods=['PATCH'])
def activate_provider(provider_id):
    try:
        provider = provider_repo.get_provider_by_id(provider_id)
        if provider is None:
            return jsonify({'error': 'provider not found'}), 404
        success = provider_repo.activate_provider(provider_id)
        if not success:
            return jsonify({'error': 'provider activation update failed'}), 400
        provider = provider_repo.get_provider_by_id(provider_id)
        return jsonify({"message": "provider activated successfully",
                        "provider": provider.to_dict()}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/providers/<provider_id>/deactivate', methods=['PATCH'])
def deactivate_provider(provider_id):
    try:
        provider = provider_repo.get_provider_by_id(provider_id)
        if provider is None:
            return jsonify({'error': 'provider not found'}), 404
        success = provider_repo.deactivate_provider(provider_id)
        if not success:
            return jsonify({'error': 'provider deactivation update failed'}), 400
        provider = provider_repo.get_provider_by_id(provider_id)
        return jsonify({"message": "provider deactivated successfully",
                        "provider": provider.to_dict()}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


### jobs ###

@app.route('/jobs', methods=['GET'])
def get_jobs():
    try:
        status = request.args.get('status')
        jobs = []
        jobs_to_dict = []
        if status in StatusList:
            jobs = job_repo.get_jobs_by_status(status)
        else:
            jobs = job_repo.get_all_jobs()

        for job in jobs:
            jobs_to_dict.append(job.to_dict())
        return jsonify({"jobs": jobs_to_dict}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/jobs', methods=['POST'])
def create_job():
    try:
        data = request.get_json()
        new_job = system.create_job(**data)
        success = job_repo.create_job(new_job)
        if not success:
            return jsonify({'error': 'job creation failed'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    return jsonify(
        {"message": "job created successfully",
         "job": new_job.to_dict()
         }), 201


@app.route('/jobs/<job_id>/assign/<provider_id>', methods=['POST'])
def assign_provider_to_job(job_id, provider_id):
    try:
        job = job_repo.get_job_by_id(job_id)
        if job is None:
            return jsonify({'error': 'job not found'}), 404
        provider = provider_repo.get_provider_by_id(provider_id)
        if provider is None:
            return jsonify({'error': 'provider not found'}), 404
        success = job_repo.assign_provider_to_job(job_id, provider_id)
        if not success:
            return jsonify({'error': 'job assignment failed'}), 400
        job = job_repo.get_job_by_id(job_id)
        return jsonify({"message": "job assigned successfully",
                        "job": job.to_dict()
                        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/jobs/<job_id>/start', methods=['POST'])
def start_job(job_id):
    try:
        job = job_repo.get_job_by_id(job_id)
        if job is None:
            return jsonify({'error': 'job not found'}), 404
        success = job_repo.start_job(job)
        if not success:
            return jsonify({'error': 'job start failed'}), 400
        job = job_repo.get_job_by_id(job_id)
        return jsonify({"message": "job started successfully",
                        "job": job.to_dict()
                        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/jobs/<job_id>/complete', methods=['POST'])
def complete_job(job_id):
    try:
        job = job_repo.get_job_by_id(job_id)
        if job is None:
            return jsonify({'error': 'job not found'}), 404
        success = job_repo.complete_job(job)
        if not success:
            return jsonify({'error': 'job completion failed'}), 400
        job = job_repo.get_job_by_id(job_id)
        return jsonify({"message": "job completed successfully",
                        "job": job.to_dict()
                        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/jobs/<job_id>/cancel', methods=['POST'])
def cancel_job(job_id):
    try:
        job = job_repo.get_job_by_id(job_id)
        if job is None:
            return jsonify({'error': 'job not found'}), 404
        success = job_repo.cancel_job(job)
        if not success:
            return jsonify({'error': 'job cancellation failed'}), 400
        job = job_repo.get_job_by_id(job_id)
        return jsonify({"message": "job canceled successfully",
                        "job": job.to_dict()
                        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/jobs/<job_id>/price', methods=['PATCH'])
def update_job_price(job_id):
    try:
        data = request.get_json()
        job = job_repo.get_job_by_id(job_id)
        if job is None:
            return jsonify({'error': 'job not found'}), 404
        new_price = data['price']
        success = job_repo.update_job_price(job_id, new_price)
        if not success:
            return jsonify({'error': 'job update failed'}), 400
        job = job_repo.get_job_by_id(job_id)
        return jsonify({"message": "job price updated successfully",
                        "job": job.to_dict()}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/jobs/<job_id>/address', methods=['PATCH'])
def update_job_address(job_id):
    try:
        data = request.get_json()
        job = job_repo.get_job_by_id(job_id)
        if job is None:
            return jsonify({'error': 'job not found'}), 404
        address = data['address']
        success = job_repo.update_job_address(job_id, address)
        if not success:
            return jsonify({'error': 'job update failed'}), 400
        job = job_repo.get_job_by_id(job_id)
        return jsonify({"message": "address job updated successfully",
                        "job": job.to_dict()}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


# @app.route('/jobs/<job_id>/description', methods=['PATCH'])
# def update_job_description(job_id):
    try:
        data = request.get_json()
        job = job_repo.get_job_by_id(job_id)
        if job is None:
            return jsonify({'error': 'job not found'}), 404
        description = data['description']
        success = job_repo.update_job_description(job_id, description)
        if not success:
            return jsonify({'error': 'job update failed'}), 400
        job = job_repo.get_job_by_id(job_id)
        return jsonify({"message": "description job updated successfully",
                        "job": job.to_dict()}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/jobs/<job_id>/schedule', methods=['PATCH'])
def update_job_schedule(job_id)
    try:
        data = request.get_json()
        job = job_repo.get_job_by_id(job_id)
        if job is None:
            return jsonify({'error': 'job not found'}), 404
        new_schedule = data['schedule_date']
        new_schedule = datetime.fromisoformat(new_schedule)
        success = job_repo.update_schedule_job(job_id, new_schedule)
        if not success:
            return jsonify({'error': 'job update failed'}), 400
        job = job_repo.get_job_by_id(job_id)
        return jsonify({"message": "schedule job updated successfully",
                        "job": job.to_dict()}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# @app.route('/jobs/open_jobs', methods=['GET'])
# def open_jobs():
