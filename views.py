from django.shortcuts import get_object_or_404, render
from django.db.models import Q

from .models import ExcludedParty


def provider_search(request):
    first_name = request.GET.get("first_name", "").strip()
    last_name = request.GET.get("last_name", "").strip()
    business_name = request.GET.get("business_name", "").strip()
    npi = request.GET.get("npi", "").strip()

    results = ExcludedParty.objects.none()

    if first_name or last_name or business_name or npi:
        results = ExcludedParty.objects.all()

        if first_name:
            results = results.filter(first_name__icontains=first_name)

        if last_name:
            results = results.filter(last_name__icontains=last_name)

        if business_name:
            results = results.filter(business_name__icontains=business_name)

        if npi:
            results = results.filter(
                identifier__identifier_type__iexact="NPI",
                identifier__identifier_value__icontains=npi,
            )

        results = results.distinct()[:100]

    return render(
        request,
        "providers/search.html",
        {
            "first_name": first_name,
            "last_name": last_name,
            "business_name": business_name,
            "npi": npi,
            "results": results,
        },
    )

def provider_detail(request, party_id):
    provider = get_object_or_404(
        ExcludedParty,
        party_id=party_id
    )

    identifiers = provider.identifier_set.all()
    exclusions = provider.exclusionrecord_set.select_related(
        "data_source",
        "import_log"
    ).all()

    return render(
        request,
        "providers/detail.html",
        {
            "provider": provider,
            "identifiers": identifiers,
            "exclusions": exclusions,
        },
    )
