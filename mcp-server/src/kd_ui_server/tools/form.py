"""Form generation tool for Flask templates with DaisyUI."""


def create_form(form_type="custom", fields=None, method="POST", action="", inline=False):
    """
    Generate a beautiful form template.
    
    Args:
        form_type: "login", "register", "contact", "settings", or "custom"
        fields: List of field configurations
        method: "POST" or "GET"
        action: Form submission URL
        inline: Display fields inline or stacked
    
    Returns:
        Form template string
    """
    if fields is None:
        fields = []
    
    # Use predefined form if specified
    if form_type == "login" and not fields:
        return _generate_login_form(action)
    elif form_type == "register" and not fields:
        return _generate_register_form(action)
    elif form_type == "contact" and not fields:
        return _generate_contact_form(action)
    
    # Generate custom form
    return _generate_custom_form(fields, method, action, inline)


def _generate_login_form(action):
    """Generate a login form."""
    return '''
<div class="flex items-center justify-center min-h-screen bg-base-200">
  <div class="card w-96 bg-base-100 shadow-xl">
    <div class="card-body">
      <h2 class="card-title justify-center text-2xl font-bold mb-4">Login</h2>
      <form method="POST" action="''' + action + '''">
        {% if csrf_token %}
        <input type="hidden" name="csrf_token" value="{{ csrf_token }}"/>
        {% endif %}
        
        <div class="form-control w-full">
          <label class="label">
            <span class="label-text">Email</span>
          </label>
          <input type="email" name="email" placeholder="email@example.com" class="input input-bordered w-full" required />
        </div>
        
        <div class="form-control w-full mt-4">
          <label class="label">
            <span class="label-text">Password</span>
          </label>
          <input type="password" name="password" placeholder="••••••••" class="input input-bordered w-full" required />
          <label class="label">
            <a href="/forgot-password" class="label-text-alt link link-hover">Forgot password?</a>
          </label>
        </div>
        
        {% if error %}
        <div class="alert alert-error mt-4">
          <svg xmlns="http://www.w3.org/2000/svg" class="stroke-current shrink-0 h-6 w-6" fill="none" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
          <span>{{ error }}</span>
        </div>
        {% endif %}
        
        <div class="form-control mt-6">
          <button type="submit" class="btn btn-primary">Login</button>
        </div>
        
        <div class="divider">OR</div>
        
        <div class="text-center">
          <p class="text-sm">Don't have an account? <a href="/register" class="link link-primary">Register</a></p>
        </div>
      </form>
    </div>
  </div>
</div>
'''


def _generate_register_form(action):
    """Generate a registration form."""
    return '''
<div class="flex items-center justify-center min-h-screen bg-base-200">
  <div class="card w-96 bg-base-100 shadow-xl">
    <div class="card-body">
      <h2 class="card-title justify-center text-2xl font-bold mb-4">Create Account</h2>
      <form method="POST" action="''' + action + '''">
        {% if csrf_token %}
        <input type="hidden" name="csrf_token" value="{{ csrf_token }}"/>
        {% endif %}
        
        <div class="form-control w-full">
          <label class="label">
            <span class="label-text">Full Name</span>
          </label>
          <input type="text" name="name" placeholder="John Doe" class="input input-bordered w-full" required />
        </div>
        
        <div class="form-control w-full mt-4">
          <label class="label">
            <span class="label-text">Email</span>
          </label>
          <input type="email" name="email" placeholder="email@example.com" class="input input-bordered w-full" required />
        </div>
        
        <div class="form-control w-full mt-4">
          <label class="label">
            <span class="label-text">Password</span>
          </label>
          <input type="password" name="password" placeholder="••••••••" class="input input-bordered w-full" required />
        </div>
        
        <div class="form-control w-full mt-4">
          <label class="label">
            <span class="label-text">Confirm Password</span>
          </label>
          <input type="password" name="confirm_password" placeholder="••••••••" class="input input-bordered w-full" required />
        </div>
        
        <div class="form-control mt-4">
          <label class="label cursor-pointer justify-start gap-2">
            <input type="checkbox" name="terms" class="checkbox checkbox-primary" required />
            <span class="label-text">I agree to the Terms and Conditions</span>
          </label>
        </div>
        
        {% if error %}
        <div class="alert alert-error mt-4">
          <span>{{ error }}</span>
        </div>
        {% endif %}
        
        <div class="form-control mt-6">
          <button type="submit" class="btn btn-primary">Create Account</button>
        </div>
        
        <div class="divider">OR</div>
        
        <div class="text-center">
          <p class="text-sm">Already have an account? <a href="/login" class="link link-primary">Login</a></p>
        </div>
      </form>
    </div>
  </div>
</div>
'''


def _generate_contact_form(action):
    """Generate a contact form."""
    return '''
<div class="max-w-2xl mx-auto p-6">
  <div class="card bg-base-100 shadow-xl">
    <div class="card-body">
      <h2 class="card-title text-2xl font-bold mb-4">Contact Us</h2>
      <form method="POST" action="''' + action + '''">
        {% if csrf_token %}
        <input type="hidden" name="csrf_token" value="{{ csrf_token }}"/>
        {% endif %}
        
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div class="form-control w-full">
            <label class="label">
              <span class="label-text">First Name</span>
            </label>
            <input type="text" name="first_name" placeholder="John" class="input input-bordered w-full" required />
          </div>
          
          <div class="form-control w-full">
            <label class="label">
              <span class="label-text">Last Name</span>
            </label>
            <input type="text" name="last_name" placeholder="Doe" class="input input-bordered w-full" required />
          </div>
        </div>
        
        <div class="form-control w-full mt-4">
          <label class="label">
            <span class="label-text">Email</span>
          </label>
          <input type="email" name="email" placeholder="email@example.com" class="input input-bordered w-full" required />
        </div>
        
        <div class="form-control w-full mt-4">
          <label class="label">
            <span class="label-text">Subject</span>
          </label>
          <input type="text" name="subject" placeholder="How can we help?" class="input input-bordered w-full" required />
        </div>
        
        <div class="form-control w-full mt-4">
          <label class="label">
            <span class="label-text">Message</span>
          </label>
          <textarea name="message" placeholder="Your message here..." class="textarea textarea-bordered h-32" required></textarea>
        </div>
        
        {% if success %}
        <div class="alert alert-success mt-4">
          <span>{{ success }}</span>
        </div>
        {% endif %}
        
        {% if error %}
        <div class="alert alert-error mt-4">
          <span>{{ error }}</span>
        </div>
        {% endif %}
        
        <div class="card-actions justify-end mt-6">
          <button type="reset" class="btn btn-ghost">Clear</button>
          <button type="submit" class="btn btn-primary">Send Message</button>
        </div>
      </form>
    </div>
  </div>
</div>
'''


def _generate_custom_form(fields, method, action, inline):
    """Generate a custom form based on field specifications."""
    form_class = "grid grid-cols-1 md:grid-cols-2 gap-4" if inline else ""
    
    form_html = f'''
<div class="max-w-4xl mx-auto p-6">
  <div class="card bg-base-100 shadow-xl">
    <div class="card-body">
      <h2 class="card-title text-2xl font-bold mb-4">Form</h2>
      <form method="{method}" action="{action}">
        {{% if csrf_token %}}
        <input type="hidden" name="csrf_token" value="{{{{ csrf_token }}}}"/>
        {{% endif %}}
        
        <div class="{form_class}">
'''
    
    for field in fields:
        field_name = field.get("name", "")
        field_type = field.get("type", "text")
        label = field.get("label", "")
        placeholder = field.get("placeholder", "")
        required = field.get("required", False)
        options = field.get("options", [])
        
        required_attr = "required" if required else ""
        
        if field_type in ["text", "email", "password", "number"]:
            form_html += f'''
          <div class="form-control w-full">
            <label class="label">
              <span class="label-text">{label}</span>
            </label>
            <input type="{field_type}" name="{field_name}" placeholder="{placeholder}" class="input input-bordered w-full" {required_attr} />
          </div>
'''
        
        elif field_type == "textarea":
            form_html += f'''
          <div class="form-control w-full {'md:col-span-2' if inline else ''}">
            <label class="label">
              <span class="label-text">{label}</span>
            </label>
            <textarea name="{field_name}" placeholder="{placeholder}" class="textarea textarea-bordered h-24" {required_attr}></textarea>
          </div>
'''
        
        elif field_type == "select":
            form_html += f'''
          <div class="form-control w-full">
            <label class="label">
              <span class="label-text">{label}</span>
            </label>
            <select name="{field_name}" class="select select-bordered w-full" {required_attr}>
              <option value="">Select {label}</option>
'''
            for option in options:
                form_html += f'              <option value="{option}">{option}</option>\n'
            form_html += '''            </select>
          </div>
'''
        
        elif field_type == "checkbox":
            form_html += f'''
          <div class="form-control">
            <label class="label cursor-pointer justify-start gap-2">
              <input type="checkbox" name="{field_name}" class="checkbox checkbox-primary" {required_attr} />
              <span class="label-text">{label}</span>
            </label>
          </div>
'''
        
        elif field_type == "file":
            form_html += f'''
          <div class="form-control w-full">
            <label class="label">
              <span class="label-text">{label}</span>
            </label>
            <input type="file" name="{field_name}" class="file-input file-input-bordered w-full" {required_attr} />
          </div>
'''
    
    form_html += '''
        </div>
        
        {% if error %}
        <div class="alert alert-error mt-4">
          <span>{{ error }}</span>
        </div>
        {% endif %}
        
        <div class="card-actions justify-end mt-6">
          <button type="reset" class="btn btn-ghost">Reset</button>
          <button type="submit" class="btn btn-primary">Submit</button>
        </div>
      </form>
    </div>
  </div>
</div>
'''
    
    return form_html
