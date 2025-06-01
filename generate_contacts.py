def generate_vcf_content(num_contacts):
    vcf_entries = []
    base_phone_number = 17634782391  # Start with a number to avoid leading zero issues in incrementing

    for i in range(1, num_contacts + 1):
        phone_number_str = f"0{base_phone_number + i - 1}" # Add back leading zero for display
        # Use phone number as N and FN
        contact_name_n = phone_number_str
        contact_name_fn = phone_number_str

        vcf_entry = f"""BEGIN:VCARD
VERSION:3.0
N:{contact_name_n}
FN:{contact_name_fn}
TEL;TYPE=CELL:{phone_number_str}
END:VCARD"""
        vcf_entries.append(vcf_entry)

    return "\n".join(vcf_entries)

if __name__ == "__main__":
    content = generate_vcf_content(100)
    with open("contacts.vcf", "w") as f:
        f.write(content)
    print(f"{len(content.split('END:VCARD')) -1 } contacts generated and saved to contacts.vcf with phone numbers as names.")
